# Hypotheses — Plugin Skills Overlap

<!-- Paths in this file are relative to THIS file's location (hypotheses/<slug>.md). -->

## Meta
- Feature: `../knowledge/product/features/skills-architecture.md`
- Status: active
- Created: 2026-06-29
- Last updated: 2026-06-29

## Value risk
### H-V1: Redundant skills cause the AI agent to choose the wrong skill for the task, degrading performance
- **Origin:** data-derived (from user observation)
- **Confidence:** medium
- **Evidence for:**
  - The framework contains overlapping skills (e.g., `product_brainstorm` vs `eng_brainstorming`, `product_derive-tests` vs `eng_test-driven-development`) `(chat, no artifact)`
  - Agents given too many similar tools suffer from decision fatigue and context bloat `(industry-knowledge)`
- **Evidence against:**
  - _(none yet)_
- **Open questions / caveats:**
  - Are the underlying system prompts for `eng_brainstorming` strictly engineering-focused while `product_brainstorm` is strategy-focused? We don't know if the separation of concerns is actually maintained at execution time.
- **Test:** Run identical prompts through both skills and measure divergence in output shape.
- **Decision trigger:** If outputs are functionally identical, merge them.
- **Status:** archived
- **Resolution:** Invalidated by code analysis (see decisions/2026-06-29-skills-overlap.md). The overlap is false; the tools serve completely different lifecycle phases.

## Usability risk
### H-U1: PMs and Engineers are confused about which namespace to use when triggering tasks
- **Origin:** proactive
- **Confidence:** low
- **Evidence for:**
  - _(none yet)_
- **Evidence against:**
  - _(none yet)_
- **Open questions / caveats:**
  - Is the user acting as a solo founder, or are multiple people using the plugin? If it's a solo founder, the namespace boundary might be entirely artificial.
- **Test:** Observe user command usage. If users mix `eng_` and `product_` commands in the same thought process, the boundaries are artificial.
- **Decision trigger:** If users consistently guess the wrong prefix, simplify the prefix taxonomy.
- **Status:** archived
- **Resolution:** Resolved. We kept the tools but aggressively updated the YAML descriptions to highlight the boundaries (e.g. [STATE ROUTING] vs [TEXT GENERATION]).

## Feasibility risk
### H-F1: Maintaining separate cognitive contexts for Product, Engineering, and Brain is impossible for a single context-window
- **Origin:** proactive
- **Confidence:** medium
- **Evidence for:**
  - Loading both `AGENTS.md` (Brain) and `eng_` guidelines simultaneously risks exceeding the context budget and confusing the system prompt `(industry-knowledge)`
- **Evidence against:**
  - _(none yet)_
- **Open questions / caveats:**
  - Can subagents fully isolate the engineering context from the product context?
- **Test:** Check token count and instruction following when both an engineering task and a product task are requested in the same session.
- **Decision trigger:** If context bleed occurs, enforce strict subagent boundaries for each domain.
- **Status:** active
- **Resolution:** 

## Viability risk
### H-B1: The framework becomes too heavy to maintain due to duplicated skill code
- **Origin:** proactive
- **Confidence:** medium
- **Evidence for:**
  - The migration created 58 total skills; maintaining dual versions of test derivation, planning, and brainstorming increases maintenance burden `(chat, no artifact)`
- **Evidence against:**
  - _(none yet)_
- **Open questions / caveats:**
  - How many skills share >80% of their instructional content?
- **Test:** Run a diff comparison across suspected overlap skills.
- **Decision trigger:** If significant code duplication exists, extract shared logic into `references/` or merge the skills.
- **Status:** archived
- **Resolution:** Invalidated. Diff analysis showed no significant code duplication; the skills are distinct implementations.

## Other risk (Epistemic risk)
### H-O1: Overlapping ingestion skills cause knowledge fragmentation
- **Origin:** proactive
- **Confidence:** high
- **Evidence for:**
  - `brain_ingest` exists alongside `product_interview`, `product_meeting-notes`, and `product_triage-requests` `(chat, no artifact)`
- **Evidence against:**
  - _(none yet)_
- **Open questions / caveats:**
  - Does `product_interview` route observations to `knowledge/users/insights.md` the way `brain_ingest` does? If not, the brain will lose track of user signals.
- **Test:** Audit the `SKILL.md` of `product_interview` to see if it respects the Brain canonical storage rules.
- **Decision trigger:** If `product_*` ingestion tools bypass `brain/` routing rules, deprecate them in favor of `brain_ingest`.
- **Status:** archived
- **Resolution:** Invalidated. `product_interview` formats text; it relies on `brain_ingest` to actually route the formatted text into the brain. They are synergistic, not fragmented.
