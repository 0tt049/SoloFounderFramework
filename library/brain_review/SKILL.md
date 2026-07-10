---
name: brain_review
description: "Run a weekly review of the product brain. Cleans up stale evidence, archives features, and surfaces strategy drift."
---

# review workflow

## `/review`
- **Loads:** everything modified in the last 30 days; full hypothesis and decision indexes.
- **Updates:** direct edits where confidence is high; `maintenance/log/YYYY-MM-DD.md` always.
- **Surfaces:** stale evidence, hypothesis hygiene gaps, stakeholder relationship debt, strategy tensions, compression candidates, archival candidates.
- **Conversational:** "Run a weekly review" or "Let's clean up the brain."
