---
title: "GCal Organizer"
description: "CLI tool for automated meeting note organization and calendar sync"
weight: 4
---

## GCal Organizer

GCal Organizer is a Go CLI tool that automates meeting note organization, calendar attachment syncing, AI-powered task assignment, and decision extraction using Google Workspace APIs and Gemini AI.

### Workflow

1. **Organize** -- Finds meeting docs in Drive and organizes them into topic-based folders
2. **Sync Calendar** -- Links calendar attachments to meeting folders, shares with attendees
3. **Assign Tasks** -- Locates checkbox action items in Google Docs and assigns them via Gemini AI
4. **Extract Decisions** -- Extracts decisions from meeting transcripts and creates categorized "Decisions" tabs

### Key Features

- **Automatic folder routing** -- Documents named `Topic - YYYY-MM-DD` are organized into topic folders
- **Calendar attachment sync** -- Links calendar attachments as shortcuts in meeting folders
- **AI-powered task assignment** -- Uses Gemini to identify assignees from checkbox items
- **Decision extraction** -- Categorizes transcript decisions into Made, Deferred, and Open Items
- **Runs as hourly service** -- `gcal-organizer install` sets up a background service on macOS/Linux
- **Secure credential storage** -- OAuth tokens stored in OS keychain by default

### Installation

```bash
brew tap jflowers/gcal-organizer
brew install --cask gcal-organizer
```

### Links

- [GitHub](https://github.com/jflowers/gcal-organizer)
