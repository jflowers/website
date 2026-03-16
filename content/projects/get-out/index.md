---
title: "Get Out"
description: "CLI tool to export Slack messages to Google Docs"
weight: 3
---

## Get Out

Get Out is a CLI tool to export Slack messages (DMs, groups, channels) to Google Docs with an organized folder structure.

### Key Features

- **Browser-based extraction** -- Access DMs and private group messages via Chrome DevTools Protocol
- **API-based extraction** -- Access public/private channels via Slack bot token
- **Google Drive integration** -- Creates organized folder hierarchy with daily Google Docs
- **Thread support** -- Exports threads to separate subfolders with linked references
- **@Mention linking** -- Converts `@mentions` to clickable Google email links
- **Cross-conversation link resolution** -- Second-pass scan resolves forward references across conversations
- **Batch and parallel export** -- `--all-dms`, `--all-groups`, and `--parallel N` for bulk exports
- **Checkpoint/Resume** -- Granular checkpointing after each doc with `--resume` for crash recovery
- **Incremental sync** -- `--sync` mode exports only new messages since last run

### Installation

```bash
brew tap jflowers/tools
brew install get-out
```

### Links

- [GitHub](https://github.com/jflowers/get-out)
