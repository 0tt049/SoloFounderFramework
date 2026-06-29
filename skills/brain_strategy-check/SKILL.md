---
name: brain_strategy-check
description: "Check recent decisions and ingested signals against the stated product strategy to identify and flag strategy drift."
---

# strategy-check workflow

## `/strategy-check`
- **Loads:** last 30 days of decisions + ingested signals, `knowledge/strategy.md`.
- **Updates:** appends to `strategy.md § Tensions` only when threshold met.
- **Surfaces:** divergence between recent work and stated strategy.
- **Conversational:** "Are we drifting from strategy?"
