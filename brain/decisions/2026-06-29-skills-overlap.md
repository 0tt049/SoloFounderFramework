# Decision: Resolve Skill Overlap Between Domains

## Status
decided

## Date
2026-06-29

## Context
The framework currently contains 58 skills. An audit was raised concerning potential functional overlap between `brain_`, `product_`, and `eng_` namespaces (e.g., `product_brainstorm` vs `eng_brainstorming`, `product_derive-tests` vs `eng_test-driven-development`, `brain_ingest` vs `product_interview`).

## Options considered
1. **Merge overlapping skills**: Consolidate redundant skills.
2. **Keep and Clarify**: Maintain the distinct tools but dramatically emphasize their distinct boundaries in their metadata descriptions.

## Decision
**Keep and Clarify**. The overlap is a "false overlap." The tools use similar terminology but operate at entirely different stages of the development lifecycle and serve distinct purposes (e.g., text formatting vs state routing; coverage auditing vs code writing; product strategy vs technical specification). We will update the YAML descriptions to explicitly state these boundaries so agents and users do not confuse them.

## Why
A code analysis of the `SKILL.md` files proved there is no actual functional duplication.
- `brain_ingest` is a strict state router, while `product_interview` is a text formatter.
- `product_derive-tests` builds an audit map based on docs, while `eng_test-driven-development` executes the Red-Green-Refactor coding cycle.
- `product_brainstorm` decides *what* features to build (strategy), while `eng_brainstorming` decides *how* to build them (architecture).
Merging them would conflate strategy with execution.

## Evidence
- Diff analysis of `brain_ingest`, `product_interview`, `product_derive-tests`, `eng_test-driven-development`, `product_brainstorm`, and `eng_brainstorming` confirms distinct operational phases.  (chat, no artifact)

## Explicitly NOT doing
- We are not merging any of the skills.  (chat, no artifact)
- We are not restricting tools to specific subagents (yet).  (chat, no artifact)

## What would reverse this
If agent usage logs still show the AI attempting to write code using `product_derive-tests` instead of `eng_test-driven-development`, indicating the YAML descriptions are not a strong enough deterrent.

## Remaining ambiguities
- None for these specific 3 pairs.

## Linked
- Hypotheses: `../hypotheses/skills-overlap.md`
