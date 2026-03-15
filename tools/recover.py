#!/usr/bin/env python3
"""
jayflowers.com Content Recovery Tool

Recovers archived content from the Wayback Machine and converts it
into Hugo-compatible Markdown page bundles.

Usage:
    python3 tools/recover.py manifest     # Step 1: Build URL manifest from CDX API
    python3 tools/recover.py fetch        # Step 2: Fetch raw HTML from Wayback Machine
    python3 tools/recover.py convert      # Step 3: Convert HTML to Hugo Markdown bundles
    python3 tools/recover.py all          # Run all steps
"""

import json
import os
import re
import sys
import time
import urllib.parse
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup, Comment
import markdownify

# ── Configuration ──────────────────────────────────────────────────────────

DOMAIN = "jayflowers.com"
CDX_API = "https://web.archive.org/cdx/search/cdx"
WAYBACK_BASE = "https://web.archive.org/web"

PROJECT_ROOT = Path(__file__).parent.parent
TOOLS_DIR = PROJECT_ROOT / "tools"
RAW_DIR = TOOLS_DIR / "raw_html"
MANIFEST_FILE = TOOLS_DIR / "manifest.json"
CONTENT_DIR = PROJECT_ROOT / "content"

# Rate limiting: be polite to the Wayback Machine
REQUEST_DELAY = 0.5  # seconds between requests

HEADERS = {"User-Agent": "jayflowers.com-recovery/1.0 (content restoration project)"}


# ── Step 1: Build Manifest ─────────────────────────────────────────────────


def build_manifest():
    """Query the Wayback Machine CDX API to build a manifest of all recoverable URLs."""
    print("Building manifest from Wayback Machine CDX API...")

    manifest = {
        "wordpress": [],
        "dokuwiki": [],
        "joomla_content": [],
        "images": [],
    }

    # -- WordPress posts --
    print("  Fetching WordPress post index...")
    wp_urls = cdx_query(
        url=f"{DOMAIN}/WordPress/",
        matchType="prefix",
        filters=["statuscode:200", "mimetype:text/html"],
        collapse="urlkey",
        limit=500,
    )

    # Extract unique post URLs (only ?p=NNN, skip replytocom, paged, cat, feed, etc.)
    seen_posts = set()
    for entry in wp_urls:
        original = entry["original"]
        # Match ?p=NNN (individual posts)
        m = re.search(r"\?p=(\d+)$", original)
        if m:
            post_id = m.group(1)
            if post_id not in seen_posts:
                seen_posts.add(post_id)
                manifest["wordpress"].append(
                    {
                        "type": "wordpress",
                        "post_id": int(post_id),
                        "original_url": original,
                        "timestamp": entry["timestamp"],
                        "wayback_url": f"{WAYBACK_BASE}/{entry['timestamp']}/{original}",
                    }
                )

        # Also capture category listing pages for reference
        m_cat = re.search(r"\?cat=(\d+)$", original)
        if m_cat and "paged" not in original:
            pass  # We'll get post titles from individual post pages

        # Also capture monthly archives for discovery
        m_month = re.search(r"\?m=(\d{6})$", original)
        if m_month:
            pass  # Monthly archives help discover posts but we have individual URLs

    # Sort by post ID
    manifest["wordpress"].sort(key=lambda x: x["post_id"])
    print(f"    Found {len(manifest['wordpress'])} unique WordPress posts")

    # -- DokuWiki articles --
    print("  Fetching DokuWiki article index...")
    doku_urls = cdx_query(
        url=f"{DOMAIN}/doku/doku.php",
        matchType="prefix",
        filters=["statuscode:200", "mimetype:text/html"],
        collapse="urlkey",
        limit=500,
    )

    seen_wiki = set()
    for entry in doku_urls:
        original = entry["original"]
        # Match ?id=SLUG (article pages, not backlink/export/index actions)
        m = re.search(r"\?id=([^&]+)$", original)
        if m:
            slug = m.group(1)
            # Skip empty id, and skip if it's just a session-parameterized duplicate
            if slug and slug not in seen_wiki and "DokuWiki=" not in original:
                seen_wiki.add(slug)
                manifest["dokuwiki"].append(
                    {
                        "type": "dokuwiki",
                        "slug": slug,
                        "original_url": original,
                        "timestamp": entry["timestamp"],
                        "wayback_url": f"{WAYBACK_BASE}/{entry['timestamp']}/{original}",
                    }
                )

    # For DokuWiki pages with DokuWiki= session params, also pick them up
    # if we haven't seen the slug yet (use earliest/cleanest version)
    for entry in doku_urls:
        original = entry["original"]
        m = re.search(r"\?id=([^&]+)&", original)
        if m:
            slug = m.group(1)
            if slug and slug not in seen_wiki and "do=" not in original:
                seen_wiki.add(slug)
                manifest["dokuwiki"].append(
                    {
                        "type": "dokuwiki",
                        "slug": slug,
                        "original_url": original,
                        "timestamp": entry["timestamp"],
                        "wayback_url": f"{WAYBACK_BASE}/{entry['timestamp']}/{original}",
                    }
                )

    manifest["dokuwiki"].sort(key=lambda x: x["slug"])
    print(f"    Found {len(manifest['dokuwiki'])} unique DokuWiki articles")

    # -- Joomla content pages --
    print("  Fetching Joomla content index...")
    joomla_urls = cdx_query(
        url=f"{DOMAIN}/joomla/",
        matchType="prefix",
        filters=["statuscode:200", "mimetype:text/html"],
        collapse="urlkey",
        limit=500,
    )

    seen_joomla = set()
    for entry in joomla_urls:
        original = entry["original"]
        # Match com_content&task=view&id=NN (individual articles)
        m = re.search(r"com_content&task=view&id=(\d+)", original)
        if m:
            article_id = m.group(1)
            if article_id not in seen_joomla:
                seen_joomla.add(article_id)
                manifest["joomla_content"].append(
                    {
                        "type": "joomla",
                        "article_id": int(article_id),
                        "original_url": original,
                        "timestamp": entry["timestamp"],
                        "wayback_url": f"{WAYBACK_BASE}/{entry['timestamp']}/{original}",
                    }
                )

    manifest["joomla_content"].sort(key=lambda x: x["article_id"])
    print(f"    Found {len(manifest['joomla_content'])} unique Joomla articles")

    # -- Images --
    print("  Fetching image index...")
    img_urls = cdx_query(
        url=f"{DOMAIN}/",
        matchType="prefix",
        filters=["statuscode:200"],
        collapse="urlkey",
        limit=1000,
    )

    seen_images = set()
    image_exts = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".ico"}
    for entry in img_urls:
        original = entry["original"]
        parsed = urllib.parse.urlparse(original)
        path_lower = parsed.path.lower()
        ext = os.path.splitext(path_lower)[1]
        if ext in image_exts:
            # Normalize the path for dedup
            norm_path = urllib.parse.unquote(parsed.path)
            if norm_path not in seen_images:
                seen_images.add(norm_path)
                manifest["images"].append(
                    {
                        "type": "image",
                        "path": norm_path,
                        "original_url": original,
                        "timestamp": entry["timestamp"],
                        "wayback_url": f"{WAYBACK_BASE}/{entry['timestamp']}/{original}",
                    }
                )

    # Also grab DokuWiki media
    doku_media = cdx_query(
        url=f"{DOMAIN}/doku/lib/exe/fetch.php",
        matchType="prefix",
        filters=["statuscode:200"],
        collapse="urlkey",
        limit=200,
    )
    for entry in doku_media:
        original = entry["original"]
        m = re.search(r"media=([^&]+)", original)
        if m:
            media_name = urllib.parse.unquote(m.group(1))
            if media_name not in seen_images:
                seen_images.add(media_name)
                manifest["images"].append(
                    {
                        "type": "image",
                        "path": f"/doku/media/{media_name}",
                        "original_url": original,
                        "timestamp": entry["timestamp"],
                        "wayback_url": f"{WAYBACK_BASE}/{entry['timestamp']}/{original}",
                    }
                )

    # Also grab DokuWiki detail pages that serve images
    doku_detail = cdx_query(
        url=f"{DOMAIN}/doku/lib/exe/detail.php",
        matchType="prefix",
        filters=["statuscode:200"],
        collapse="urlkey",
        limit=200,
    )
    for entry in doku_detail:
        original = entry["original"]
        m = re.search(r"media=([^&]+)", original)
        if m:
            media_name = urllib.parse.unquote(m.group(1))
            if media_name not in seen_images:
                seen_images.add(media_name)
                # For detail.php, the actual image is served via fetch.php
                fetch_url = original.replace("detail.php", "fetch.php")
                manifest["images"].append(
                    {
                        "type": "image",
                        "path": f"/doku/media/{media_name}",
                        "original_url": fetch_url,
                        "timestamp": entry["timestamp"],
                        "wayback_url": f"{WAYBACK_BASE}/{entry['timestamp']}/{fetch_url}",
                    }
                )

    print(f"    Found {len(manifest['images'])} unique images")

    # -- Also grab downloadable assets (pptx, etc.) --
    for entry in img_urls:
        original = entry["original"]
        parsed = urllib.parse.urlparse(original)
        path_lower = parsed.path.lower()
        if (
            path_lower.endswith(".pptx")
            or path_lower.endswith(".pdf")
            or path_lower.endswith(".zip")
        ):
            norm_path = urllib.parse.unquote(parsed.path)
            if norm_path not in seen_images:
                seen_images.add(norm_path)
                manifest["images"].append(
                    {
                        "type": "asset",
                        "path": norm_path,
                        "original_url": original,
                        "timestamp": entry["timestamp"],
                        "wayback_url": f"{WAYBACK_BASE}/{entry['timestamp']}/{original}",
                    }
                )

    # Save manifest
    MANIFEST_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_FILE, "w") as f:
        json.dump(manifest, f, indent=2)

    total = (
        len(manifest["wordpress"])
        + len(manifest["dokuwiki"])
        + len(manifest["joomla_content"])
        + len(manifest["images"])
    )
    print(f"\nManifest saved to {MANIFEST_FILE}")
    print(f"Total items: {total}")
    print(f"  WordPress posts: {len(manifest['wordpress'])}")
    print(f"  DokuWiki articles: {len(manifest['dokuwiki'])}")
    print(f"  Joomla articles: {len(manifest['joomla_content'])}")
    print(f"  Images/assets: {len(manifest['images'])}")
    return manifest


def cdx_query(url, matchType="prefix", filters=None, collapse=None, limit=100):
    """Query the Wayback Machine CDX API."""
    params = {
        "url": url,
        "matchType": matchType,
        "output": "json",
        "limit": limit,
    }
    if filters:
        params["filter"] = filters
    if collapse:
        params["collapse"] = collapse

    resp = requests.get(CDX_API, params=params, headers=HEADERS, timeout=30)
    resp.raise_for_status()

    data = resp.json()
    if not data:
        return []

    # First row is headers
    headers_row = data[0]
    results = []
    for row in data[1:]:
        entry = dict(zip(headers_row, row))
        results.append(entry)

    time.sleep(0.5)  # Be polite
    return results


# ── Step 2: Fetch Raw HTML ─────────────────────────────────────────────────


def fetch_all():
    """Fetch all items in the manifest from the Wayback Machine."""
    print("Fetching content from Wayback Machine...")

    manifest = load_manifest()
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    all_items = []
    for section in ["wordpress", "dokuwiki", "joomla_content"]:
        all_items.extend(manifest.get(section, []))

    # Also fetch images
    all_items.extend(manifest.get("images", []))

    total = len(all_items)
    fetched = 0
    skipped = 0
    errors = 0

    for i, item in enumerate(all_items):
        outfile = get_raw_path(item)
        if outfile.exists():
            skipped += 1
            continue

        print(
            f"  [{i + 1}/{total}] Fetching {item.get('slug', item.get('post_id', item.get('article_id', item.get('path', '?'))))}..."
        )

        wayback_url = item["wayback_url"]
        # Use 'id_' prefix to get raw original content without Wayback toolbar
        wayback_url = re.sub(
            r"(web\.archive\.org/web/)(\d+)/",
            r"\g<1>\g<2>id_/",
            wayback_url,
        )

        success = False
        for attempt in range(3):
            try:
                resp = requests.get(wayback_url, headers=HEADERS, timeout=30)
                resp.raise_for_status()

                outfile.parent.mkdir(parents=True, exist_ok=True)

                if item["type"] == "image" or item["type"] == "asset":
                    with open(outfile, "wb") as f:
                        f.write(resp.content)
                else:
                    with open(outfile, "w", encoding="utf-8") as f:
                        f.write(resp.text)

                fetched += 1
                success = True
                time.sleep(REQUEST_DELAY)
                break

            except Exception as e:
                if attempt < 2:
                    wait = REQUEST_DELAY * (2 ** (attempt + 1))
                    print(f"    Retry {attempt + 1}/3 after {wait}s: {e}")
                    time.sleep(wait)
                else:
                    print(f"    ERROR (gave up): {e}")
                    errors += 1
                    time.sleep(REQUEST_DELAY * 2)

    print(
        f"\nFetch complete: {fetched} fetched, {skipped} skipped (cached), {errors} errors"
    )


def get_raw_path(item):
    """Determine the local file path for a raw fetched item."""
    if item["type"] == "wordpress":
        return RAW_DIR / "wordpress" / f"p{item['post_id']}.html"
    elif item["type"] == "dokuwiki":
        return RAW_DIR / "dokuwiki" / f"{item['slug']}.html"
    elif item["type"] == "joomla":
        return RAW_DIR / "joomla" / f"article{item['article_id']}.html"
    elif item["type"] in ("image", "asset"):
        # Preserve the path structure
        path = item["path"].lstrip("/")
        return RAW_DIR / "assets" / path
    else:
        return RAW_DIR / "other" / "unknown.html"


# ── Step 3: Convert to Hugo Markdown ───────────────────────────────────────


def convert_all():
    """Convert all fetched raw HTML into Hugo Markdown page bundles."""
    print("Converting fetched content to Hugo Markdown...")

    manifest = load_manifest()

    wp_count = convert_wordpress(manifest.get("wordpress", []))
    doku_count = convert_dokuwiki(manifest.get("dokuwiki", []))
    joomla_count = convert_joomla(manifest.get("joomla_content", []))

    print(f"\nConversion complete:")
    print(f"  WordPress: {wp_count} posts")
    print(f"  DokuWiki: {doku_count} articles")
    print(f"  Joomla: {joomla_count} articles")


def convert_wordpress(items):
    """Convert WordPress posts to Hugo Markdown."""
    count = 0
    for item in items:
        raw_path = get_raw_path(item)
        if not raw_path.exists():
            print(f"  SKIP: {raw_path} not found (not fetched yet)")
            continue

        try:
            html = raw_path.read_text(encoding="utf-8", errors="replace")
            result = parse_wordpress_post(html, item)
            if result:
                write_hugo_bundle("blog", result, item)
                count += 1
        except Exception as e:
            print(f"  ERROR converting WP post {item['post_id']}: {e}")

    return count


def parse_wordpress_post(html, item):
    """Parse a WordPress post HTML into structured data."""
    soup = BeautifulSoup(html, "html.parser")

    # Remove Wayback Machine injected elements
    strip_wayback_artifacts(soup)

    # Try to find the post title
    title = None

    # Try <title> tag first
    title_tag = soup.find("title")
    if title_tag:
        title_text = title_tag.get_text(strip=True)
        # WordPress titles often have format "BlogName > Post Title"
        if ">" in title_text:
            title = title_text.split(">", 1)[1].strip()
        elif "|" in title_text:
            title = title_text.split("|", 1)[0].strip()
        else:
            title = title_text

    # Try h2 inside the post content (common WordPress pattern)
    if not title:
        h2 = soup.find("h2")
        if h2:
            title = h2.get_text(strip=True)

    if not title:
        title = f"Post {item['post_id']}"

    # Try to extract the date
    date = None

    # Look for "filed in" metadata or similar date patterns
    for text in soup.stripped_strings:
        # Pattern: "Month DDth, YYYY" or "Month DD, YYYY"
        m = re.search(
            r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})",
            text,
        )
        if m:
            try:
                date = datetime.strptime(
                    f"{m.group(1)} {m.group(2)} {m.group(3)}", "%B %d %Y"
                )
                break
            except ValueError:
                pass

    # Try the Wayback timestamp as fallback
    if not date:
        ts = item.get("timestamp", "")
        if len(ts) >= 8:
            try:
                date = datetime.strptime(ts[:8], "%Y%m%d")
            except ValueError:
                date = datetime(2007, 1, 1)

    # Extract categories
    categories = []
    # Look for "filed in <category>" pattern
    for link in soup.find_all("a"):
        href = str(link.get("href", ""))
        if "cat=" in href:
            cat_text = link.get_text(strip=True)
            if cat_text and cat_text not in categories:
                categories.append(cat_text)

    # Extract the post body
    body_html = extract_wp_body(soup)

    # Convert to Markdown
    body_md = html_to_markdown(body_html)

    # Clean up the markdown
    body_md = clean_markdown(body_md)

    return {
        "title": title,
        "date": date,
        "categories": categories,
        "body": body_md,
        "post_id": item["post_id"],
    }


def extract_wp_body(soup):
    """Extract the main post content from WordPress HTML."""
    # Try common WordPress content containers
    # The "Simplr" theme used by this blog
    for selector in [
        {"class": "entry-content"},
        {"class": "post-content"},
        {"class": "entry"},
        {"class": "postcontent"},
        {"class": "post"},
    ]:
        content = soup.find("div", selector)
        if content:
            return str(content)

    # Try finding content between the h2 title and the comments/metadata
    h2 = soup.find("h2")
    if h2:
        # Collect siblings after the h2 until we hit comments or metadata
        parts = []
        for sibling in h2.find_next_siblings():
            # Stop at comments section, trackback section, or footer
            if sibling.name == "h2":
                break
            classes = sibling.get("class", [])
            if isinstance(classes, list):
                class_str = " ".join(classes)
            else:
                class_str = str(classes)
            if any(
                kw in class_str.lower()
                for kw in ["comment", "trackback", "respond", "footer"]
            ):
                break
            text = sibling.get_text(strip=True)
            if text and ("Post a Comment" in text or "Trackback URI" in text):
                break
            parts.append(str(sibling))
        if parts:
            return "\n".join(parts)

    # Fallback: try the body minus navigation/header/footer
    body = soup.find("body")
    if body:
        # Remove nav, header, footer, sidebar, comments
        for tag in body.find_all(["nav", "header", "footer", "aside"]):
            tag.decompose()
        for div in body.find_all(
            "div", class_=re.compile(r"comment|sidebar|nav|menu|footer|header", re.I)
        ):
            div.decompose()
        return str(body)

    return str(soup)


def convert_dokuwiki(items):
    """Convert DokuWiki articles to Hugo Markdown."""
    count = 0
    for item in items:
        raw_path = get_raw_path(item)
        if not raw_path.exists():
            print(f"  SKIP: {raw_path} not found")
            continue

        try:
            html = raw_path.read_text(encoding="utf-8", errors="replace")
            result = parse_dokuwiki_article(html, item)
            if result:
                write_hugo_bundle("wiki", result, item)
                count += 1
        except Exception as e:
            print(f"  ERROR converting DokuWiki {item['slug']}: {e}")

    return count


def parse_dokuwiki_article(html, item):
    """Parse a DokuWiki article HTML into structured data."""
    soup = BeautifulSoup(html, "html.parser")
    strip_wayback_artifacts(soup)

    # Title from the page
    title = item["slug"].replace("_", " ").title()

    # Try to get a better title from the page itself
    title_tag = soup.find("title")
    if title_tag:
        title_text = title_tag.get_text(strip=True)
        # DokuWiki titles: "slug [SiteName]"
        if "[" in title_text:
            title = title_text.split("[")[0].strip()
        elif "|" in title_text:
            title = title_text.split("|")[0].strip()

    # Extract date from "Last modified" line
    date = None
    for text in soup.stripped_strings:
        m = re.search(r"(\d{4})/(\d{2})/(\d{2})", text)
        if m:
            try:
                date = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)))
                break
            except ValueError:
                pass

    if not date:
        ts = item.get("timestamp", "")
        if len(ts) >= 8:
            try:
                date = datetime.strptime(ts[:8], "%Y%m%d")
            except ValueError:
                date = datetime(2006, 1, 1)

    # Extract body content
    body_div = soup.find("div", class_="dokuwiki")
    if not body_div:
        body_div = soup.find("div", id="dokuwiki__content")
    if not body_div:
        # Try the page div
        body_div = soup.find("div", class_="page")

    if body_div:
        # Remove DokuWiki UI elements
        for tag in body_div.find_all(
            "div", class_=re.compile(r"toc|bar|btn|secedit", re.I)
        ):
            tag.decompose()
        body_html = str(body_div)
    else:
        body_html = str(soup)

    body_md = html_to_markdown(body_html)
    body_md = clean_markdown(body_md)

    return {
        "title": title,
        "date": date,
        "categories": ["Wiki"],
        "body": body_md,
        "slug": item["slug"],
    }


def convert_joomla(items):
    """Convert Joomla content pages to Hugo Markdown."""
    count = 0
    for item in items:
        raw_path = get_raw_path(item)
        if not raw_path.exists():
            print(f"  SKIP: {raw_path} not found")
            continue

        try:
            html = raw_path.read_text(encoding="utf-8", errors="replace")
            result = parse_joomla_article(html, item)
            if result:
                write_hugo_bundle("blog", result, item)
                count += 1
        except Exception as e:
            print(f"  ERROR converting Joomla article {item['article_id']}: {e}")

    return count


def parse_joomla_article(html, item):
    """Parse a Joomla article HTML into structured data."""
    soup = BeautifulSoup(html, "html.parser")
    strip_wayback_artifacts(soup)

    title = None
    title_tag = soup.find("title")
    if title_tag:
        title = title_tag.get_text(strip=True)
        # Clean common Joomla title patterns
        for sep in [" - ", " :: "]:
            if sep in title:
                title = title.split(sep)[0].strip()

    if not title:
        h1 = soup.find("h1") or soup.find("h2")
        if h1:
            title = h1.get_text(strip=True)

    if not title:
        title = f"Article {item['article_id']}"

    date = None
    ts = item.get("timestamp", "")
    if len(ts) >= 8:
        try:
            date = datetime.strptime(ts[:8], "%Y%m%d")
        except ValueError:
            date = datetime(2007, 1, 1)

    # Extract main content
    content_div = soup.find("div", class_="contentpaneopen")
    if not content_div:
        content_div = soup.find("td", class_="contentheading")
        if content_div:
            content_div = content_div.find_parent("table")
    if not content_div:
        content_div = soup.find("div", id="content") or soup.find(
            "div", class_="content"
        )

    if content_div:
        body_html = str(content_div)
    else:
        body_html = str(soup)

    body_md = html_to_markdown(body_html)
    body_md = clean_markdown(body_md)

    return {
        "title": title,
        "date": date,
        "categories": ["Joomla Archive"],
        "body": body_md,
        "article_id": item.get("article_id"),
    }


# ── Shared Utilities ───────────────────────────────────────────────────────


def strip_wayback_artifacts(soup):
    """Remove Wayback Machine toolbar and injected scripts/styles."""
    # Remove the Wayback Machine toolbar div
    for div in soup.find_all("div", id="wm-ipp-base"):
        div.decompose()
    for div in soup.find_all("div", id="wm-ipp"):
        div.decompose()
    for div in soup.find_all("div", id="donato"):
        div.decompose()
    for div in soup.find_all("div", id="wm-btm"):
        div.decompose()

    # Remove Wayback-injected scripts
    for script in soup.find_all("script"):
        src = script.get("src", "")
        text = script.string or ""
        if "archive.org" in src or "archive.org" in text or "wombat" in text.lower():
            script.decompose()

    # Remove Wayback-injected styles
    for link in soup.find_all("link"):
        href = link.get("href", "")
        if "archive.org" in href:
            link.decompose()

    # Remove Wayback-injected comments
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        if (
            "FILE ARCHIVED ON" in str(comment)
            or "playback timance" in str(comment).lower()
        ):
            comment.extract()

    # Remove noscript tags from Wayback
    for ns in soup.find_all("noscript"):
        if "archive.org" in str(ns):
            ns.decompose()

    # Rewrite Wayback URLs back to original
    for tag in soup.find_all(["a", "img", "link"]):
        for attr in ["href", "src"]:
            val = tag.get(attr, "")
            if "web.archive.org/web/" in val:
                # Extract original URL
                m = re.search(r"web\.archive\.org/web/\d+(?:id_)?/(.*)", val)
                if m:
                    tag[attr] = m.group(1)


def html_to_markdown(html_str):
    """Convert HTML string to Markdown."""
    # Strip script/style/noscript tags before conversion
    soup = BeautifulSoup(html_str, "html.parser")
    for tag in soup.find_all(["script", "style", "noscript"]):
        tag.decompose()
    cleaned_html = str(soup)

    # Use markdownify for the conversion
    md = markdownify.markdownify(
        cleaned_html,
        heading_style="ATX",
        bullets="-",
        code_language="csharp",  # Default for .NET content
    )
    return md


def clean_markdown(md):
    """Clean up converted Markdown."""
    # Remove excessive blank lines (more than 2 in a row)
    md = re.sub(r"\n{4,}", "\n\n\n", md)

    # Remove Wayback Machine URLs that leaked through
    md = re.sub(r"https?://web\.archive\.org/web/\d+(?:id_)?/", "", md)

    # Clean up image references to use relative paths
    # e.g., http://jayflowers.com/WordPress/wp-content/uploads/... -> relative
    md = re.sub(
        r"https?://(?:www\.)?jayflowers\.com(?::80)?/WordPress/wp-content/uploads/(\S+)",
        r"images/\1",
        md,
    )
    md = re.sub(
        r"https?://(?:www\.)?jayflowers\.com(?::80)?/doku/lib/exe/fetch\.php\?[^)]+media=([^)&\s]+)",
        r"images/\1",
        md,
    )

    # Remove DotNetKicks badges
    md = re.sub(r"\[!\[kick it on DotNetKicks\.com\].*?\]\(.*?\)", "", md)

    # Remove "Post a Comment" and "Trackback URI" links
    md = re.sub(r"\[Post a Comment\]\(#respond.*?\)", "", md)
    md = re.sub(r"\[Trackback URI\]\(.*?\)", "", md)
    md = re.sub(r"Views \(\d+\)", "", md)

    # Remove WordPress theme UI artifacts
    md = re.sub(r"Your email is \*never\* published.*", "", md, flags=re.DOTALL)
    md = re.sub(r"## Post a Comment.*", "", md, flags=re.DOTALL)
    md = re.sub(r"See more on Jay\'s Home Page!", "", md)

    # Clean up "Home > About This Post" sections
    md = re.sub(r"## \[Home\].*?About This Post.*?\.", "", md, flags=re.DOTALL)

    # Remove copyright line
    md = re.sub(r"©\s*\d{4}\s*jflowers", "", md)
    md = re.sub(r"Thanks,\s*\[WordPress\].*", "", md)

    # Remove "\[ Back \]" navigation
    md = re.sub(r"\[\\?\[?\s*Back\s*\\?\]?\]\(.*?\)", "", md)

    # Wrap bare XML/HTML-like code blocks in fenced code blocks
    # This catches lines that look like XML tags but aren't inside code fences
    lines = md.split("\n")
    result_lines = []
    in_code_block = False
    xml_block = []
    in_xml_run = False

    for line in lines:
        # Track existing fenced code blocks
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            if in_xml_run:
                # Close the XML block we were building
                result_lines.append("```xml")
                result_lines.extend(xml_block)
                result_lines.append("```")
                xml_block = []
                in_xml_run = False
            result_lines.append(line)
            continue

        if in_code_block:
            result_lines.append(line)
            continue

        # Detect lines that look like XML/Ant/NAnt code
        stripped = line.strip()
        looks_like_xml = (
            stripped.startswith("<")
            and not stripped.startswith("<http")
            and not stripped.startswith("<a ")
            and not stripped.startswith("<img ")
            and not stripped.startswith("<div")
            and not stripped.startswith("<span")
            and not stripped.startswith("<br")
            and not stripped.startswith("<p>")
            and not stripped.startswith("</p>")
            and not stripped.startswith("<table")
            and not stripped.startswith("<td")
            and not stripped.startswith("<tr")
            and not stripped.startswith("<th")
            and not stripped.startswith("<!-")
            and not stripped.startswith("<em>")
            and not stripped.startswith("<strong>")
            and len(stripped) > 3
        )

        if looks_like_xml:
            if not in_xml_run:
                in_xml_run = True
            xml_block.append(line)
        else:
            if in_xml_run:
                # End of XML run, flush it as a code block
                result_lines.append("")
                result_lines.append("```xml")
                result_lines.extend(xml_block)
                result_lines.append("```")
                result_lines.append("")
                xml_block = []
                in_xml_run = False
            result_lines.append(line)

    # Flush any remaining XML block
    if in_xml_run and xml_block:
        result_lines.append("")
        result_lines.append("```xml")
        result_lines.extend(xml_block)
        result_lines.append("```")

    md = "\n".join(result_lines)

    # Final cleanup
    md = md.strip()

    return md


def slugify(text):
    """Convert text to a URL-friendly slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    text = text.strip("-")
    return text[:80]  # Limit length


def write_hugo_bundle(section, result, item):
    """Write a Hugo page bundle for the converted content."""
    title = result["title"]
    date = result["date"] or datetime(2007, 1, 1)
    date_str = date.strftime("%Y-%m-%d")

    slug = slugify(title)
    if not slug:
        slug = f"post-{item.get('post_id', item.get('article_id', item.get('slug', 'unknown')))}"

    bundle_dir = CONTENT_DIR / section / slug
    bundle_dir.mkdir(parents=True, exist_ok=True)

    # Build front matter
    front_matter = {
        "title": title,
        "date": date_str,
        "draft": False,
    }

    if result.get("categories"):
        front_matter["categories"] = result["categories"]

    # Build aliases for old URLs
    aliases = []
    if item["type"] == "wordpress":
        aliases.append(f"/WordPress/?p={item['post_id']}")
        aliases.append(f"/WordPress/index.php?p={item['post_id']}")
    elif item["type"] == "dokuwiki":
        aliases.append(f"/doku/doku.php?id={item.get('slug', '')}")
    elif item["type"] == "joomla":
        aliases.append(
            f"/joomla/index.php?option=com_content&task=view&id={item.get('article_id', '')}"
        )

    if aliases:
        front_matter["aliases"] = aliases

    # Wayback Machine provenance
    front_matter["params"] = {
        "wayback_url": item.get("wayback_url", ""),
        "original_url": item.get("original_url", ""),
        "archived_from": "Wayback Machine",
    }

    # Write the Markdown file
    md_content = "---\n"
    md_content += format_front_matter(front_matter)
    md_content += "---\n\n"
    md_content += result["body"]
    md_content += "\n"

    index_file = bundle_dir / "index.md"
    index_file.write_text(md_content, encoding="utf-8")


def format_front_matter(data, indent=0):
    """Format a dict as YAML front matter."""
    lines = []
    prefix = "  " * indent

    for key, value in data.items():
        if isinstance(value, dict):
            lines.append(f"{prefix}{key}:")
            lines.append(format_front_matter(value, indent + 1))
        elif isinstance(value, list):
            lines.append(f"{prefix}{key}:")
            for item in value:
                if isinstance(item, dict):
                    lines.append(f"{prefix}  -")
                    lines.append(format_front_matter(item, indent + 2))
                else:
                    # Escape quotes in strings
                    item_str = str(item).replace('"', '\\"')
                    lines.append(f'{prefix}  - "{item_str}"')
        elif isinstance(value, bool):
            lines.append(f"{prefix}{key}: {str(value).lower()}")
        elif isinstance(value, str):
            # Use quotes if the string contains special YAML chars
            if any(
                c in value
                for c in [
                    ":",
                    "#",
                    "{",
                    "}",
                    "[",
                    "]",
                    ",",
                    "&",
                    "*",
                    "?",
                    "|",
                    "-",
                    "<",
                    ">",
                    "=",
                    "!",
                    "%",
                    "@",
                    "`",
                    '"',
                ]
            ):
                escaped = value.replace('"', '\\"')
                lines.append(f'{prefix}{key}: "{escaped}"')
            else:
                lines.append(f"{prefix}{key}: {value}")
        else:
            lines.append(f"{prefix}{key}: {value}")

    return "\n".join(lines) + "\n"


def load_manifest():
    """Load the manifest file."""
    if not MANIFEST_FILE.exists():
        print(f"ERROR: Manifest not found at {MANIFEST_FILE}")
        print("Run 'python3 tools/recover.py manifest' first.")
        sys.exit(1)
    with open(MANIFEST_FILE) as f:
        return json.load(f)


# ── Main ───────────────────────────────────────────────────────────────────


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "manifest":
        build_manifest()
    elif command == "fetch":
        fetch_all()
    elif command == "convert":
        convert_all()
    elif command == "all":
        build_manifest()
        fetch_all()
        convert_all()
    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
