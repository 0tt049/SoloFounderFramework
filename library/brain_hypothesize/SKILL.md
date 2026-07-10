---
name: brain_hypothesize
description: "Draft or refresh hypotheses for a product feature. Evaluates value, usability, feasibility, and viability risks based on evidence."
---

# hypothesize workflow

## `/hypothesize <feature-slug>`
- **Loads:** `knowledge/product/features/<slug>.md`, existing `hypotheses/<slug>.md` (if any), relevant user insights, current metrics.
- **Updates:** drafts or refreshes `hypotheses/<slug>.md`, organized by 5 risk areas.
- **Surfaces:** which risks are unhypothesized, which evidence supports/contradicts.
- **Conversational:** "Help me think through risks for <feature>" or "What hypotheses should we have on <feature>?"
- **Note:** works pre-ship (proactive) OR post-ship (data-derived from observed behavior).
