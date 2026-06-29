# Hypotheses — Refactoring and Audit Tools Belong in Engineering

<!-- Paths in this file are relative to THIS file's location (hypotheses/<slug>.md). -->

## Meta
- Feature: `../knowledge/product/features/framework-architecture.md`
- Status: active
- Created: 2026-06-29
- Last updated: 2026-06-29

## Value risk
### H-V1: Placing code-auditing and refactoring tools in the `product_` namespace forces the LLM into a non-technical persona, degrading the quality of the audit
- **Origin:** data-derived (from user observation)
- **Confidence:** high
- **Evidence for:**
  - The user correctly pointed out that commands like `/ship-check`, `/derive-tests`, and `/performance-audit-static` have a massive overlap with ENGINEERING, and it makes little sense for them to be in PRODUCT `(chat, no artifact)`.
  - When an LLM agent is triggered via a `product_` skill, its system prompt and internal state assume a PM/Strategy posture. Asking it to parse raw code for caching inefficiencies (performance audit) or SQL injections (security audit) under this posture is sub-optimal `(industry-knowledge)`.
- **Evidence against:**
  - _(none yet)_
- **Open questions / caveats:**
  - Will renaming them to `eng_` break any internal hardcoded cross-references within other skills?
- **Test:** Rename the tools to `eng_` and observe if the technical depth of their outputs improves when triggered by the engineering subagent.
- **Decision trigger:** If the conceptual misalignment is clear, migrate these skills to the `eng_` namespace immediately.
- **Status:** active
- **Resolution:** 

## Usability risk
### H-U1: Users are confused when looking for code-quality tools because they expect to find them in the engineering namespace
- **Origin:** data-derived (from user observation)
- **Confidence:** high
- **Evidence for:**
  - The user asked "which command should I use for refactoring?" and was surprised to find that the primary discovery tool (`/ship-check`) was prefixed with `product_`.
- **Evidence against:**
  - The original logic might have been that a "PM" signs off on the shipping packet.
- **Open questions / caveats:**
  - Does a PM do a static security audit, or does an Engineer do it and hand the *results* to the PM?
- **Test:** Map the user journey for a refactor. It starts with an Engineer auditing the code, deciding how to change it (`eng_brainstorming`), and executing the change (`eng_test-driven-development`).
- **Decision trigger:** If the entire refactoring loop is an engineering task, all tools in that loop must be `eng_`.
- **Status:** active
- **Resolution:** 

## Feasibility risk
### H-F1: We cannot easily move the tools because they are deeply tangled with product documentation
- **Origin:** proactive
- **Confidence:** low
- **Evidence for:**
  - `product_document-app` and `product_derive-tests` read from and write to system architecture documents.
- **Evidence against:**
  - Engineers are the ones who write and maintain technical system architecture documents. It is entirely feasible and correct for `eng_` skills to own technical documentation.
- **Open questions / caveats:**
  - None.
- **Test:** Execute the migration and run `grep` for the old `product_` names to ensure all references are updated.
- **Decision trigger:** If references can be safely updated, proceed with the migration.
- **Status:** active
- **Resolution:** 

## Viability risk
### H-B1: (Not applicable)
- **Status:** archived

## Other risk (Epistemic risk)
### H-O1: (Not applicable)
- **Status:** archived
