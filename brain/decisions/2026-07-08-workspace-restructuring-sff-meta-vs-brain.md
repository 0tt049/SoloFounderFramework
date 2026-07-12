# Decision: Restructure SFF-META for Skill Pipeline and Create BRAIN Workspace

## Status
decided

## Date
2026-07-08

## Context
The user observed that `SFF-META` was being cluttered with high-level architectural questions, PC maintenance, and general meta-discussions, which deviate from its technical foundation. Furthermore, specialized pipeline agents like `migration_agent` and `eval_agent` are tightly coupled to the GitHub skill ingestion loop and do not belong in high-level conversational contexts.

## Options considered
1. **Option 1 (Status Quo):** Keep `SFF-META` as a general multi-purpose meta-workspace managing both the technical skill pipeline and general high-level strategy/PC maintenance.
2. **Option 2 (Strict Segregation):** Restructure `SFF-META` to focus strictly on the Skill Discovery, Adaptation, and Evaluation pipeline. Move all general strategic decisions, PC maintenance logs, and high-level architectural discussions to a dedicated, high-level `BRAIN` workspace.

## Decision
We selected **Option 2**. We will focus `SFF-META` purely on the scraping, testing, migrating, and merging of new skills, and direct all high-level open questions to a separate `BRAIN` workspace.

## Why
1. **Separation of Concerns:** Prevents SFF-META's conversational agent from being bloated with unrelated non-technical knowledge.
2. **Context Latency Reduction:** By separating the workspaces, `SFF-META` only needs to load pipeline-specific rules and tools, while the `BRAIN` workspace will load the high-level `brain_*` skills.
3. **Correct Agent Scoping:** Resolves the scoping issue where specialized tools and agents like `migration_agent` and `eval_agent` were being exposed to high-level conversational threads.

## Evidence
- User explicitly proposed this segregation to keep SFF-META focused solely on skill pipelines and use "BRAIN" for high-level questions  (stakeholder-verbal, Otavio, 2026-07-08)
- Evidence from context-bloat benchmarks proved loading too many disparate skills into a single active context degrades TTFT by ~74.9%  (chat, no artifact)

## Explicitly NOT doing
- Loading high-level PC maintenance rules or general personal knowledge rules inside `SFF-META`.  (stakeholder-verbal, Otavio, 2026-07-08)
- Invoking `migration_agent` or `eval_agent` outside the automated skill testing loop.  (stakeholder-verbal, Otavio, 2026-07-08)

## What would reverse this
If maintaining separate workspaces for the pipeline and the high-level brain introduces too much directory switching or cognitive friction for the user.

## Remaining ambiguities
- The physical setup of the `BRAIN` workspace folder and its corresponding `.agents/skills` initialization.

## Linked
- Hypotheses: `../hypotheses/dynamic-skill-activation.md`
