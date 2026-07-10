---
name: brain_ingest
description: "[STATE ROUTING] The official data router. Takes cleaned insights or raw text and commits them to the canonical knowledge base (hypotheses, stakeholders, etc). Use this to make the agent remember things."
---

# ingest workflow

## `/ingest interview <file>`
- **Loads:** the transcript file, `knowledge/users/`, active hypotheses.
- **Updates:** `knowledge/users/insights.md`, `hypotheses/<feature>.md`, `ingestion/interviews/YYYY-MM-DD-<participant>.md`.
- **Surfaces:** affected hypotheses, new candidates, persona drift detected.
- **Conversational:** "I just talked to <person>, here's the transcript / here's what they said."

## `/ingest meeting <file>`
- **Loads:** the notes, relevant stakeholder file(s), recent decisions.
- **Updates:** `stakeholders/<slug>.md`, draft `decisions/YYYY-MM-DD-<slug>.md`, `ingestion/meetings/YYYY-MM-DD-<topic>.md`.
- **Surfaces:** decisions captured (PM confirms), action items, stakeholder concerns updated.
- **Conversational:** "Here are notes from my 1:1 with <name>" or "We just decided X in standup."

## `/ingest market <url-or-file>`
- **Loads:** the artifact, relevant competitor file, `knowledge/market/`.
- **Updates:** `knowledge/market/competitors/<slug>.md` or `trends.md`, possibly `strategy.md § Tensions`.
- **Surfaces:** affected hypotheses / strategy elements, new trend candidate.
- **Conversational:** "<competitor> just launched X" or "Here's an analyst piece on the category."

## `/ingest adhoc`
- **Loads:** the dump.
- **Updates:** routes to the right area; never parks in `ingestion/adhoc/`.
- **Surfaces:** where it was routed.
- **Conversational:** "I just learned X" with no clear category.
