---
name: orchestrating-engineering-workflows
description: Orchestrates and coordinates full-stack software development tasks. Resolves ambiguity by interactively clarifying user intent, routes tasks to specialized skills, and enforces strict engineering rules like Test-Driven Development (TDD) and Clean Architecture. Trigger this when initiating any code development, starting new features, or requesting system integration.
allowed-tools: [Read, Write, Edit, Glob, AskUserQuestion]
---

# Orchestrating Engineering Workflows

## Goal
To coordinate, route, and manage all software engineering operations in the project workspace, ensuring that all code meets the high bar of clean architecture, performance, security, and TDD, and maintaining the project's documentation ledger (`CLAUDE.md`).

## When to Use This Skill
- At the start of a coding session or conversational request.
- When embarking on new product features, system architectures, or major migrations.
- When coordinating multiple specialized subagents or tools for feature execution.

### Do Not Use This Skill For:
- Simple, one-off informational queries that do not require any code modifications or pipeline orchestration.

## Plan-Validate-Execute Workflow
1. **Plan (Clarification & Routing):**
   - Interactively clarify user intent if there is any ambiguity. Present 1-3 targeted multiple-choice or short-form questions to narrow down technical specifics.
   - Map out the exact list of skills (e.g. scaffolding, coding, testing, reviewing) required to achieve the user's objective.
2. **Validate (Enforce 4 Non-Negotiables):**
   - **Performance First:** All proposed architectures and code patterns must target O(N) or O(1) complexity. Absolutely no database N+1 queries.
   - **Clean Architecture:** Mandate strict boundary isolation (e.g., domain modules cannot depend on implementation/infrastructure details).
   - **Secure by Design:** Ensure zero hardcoded secrets. Parametrize all database queries, and sanitize raw inputs.
   - **Test-Driven Always (TDD):** Every code addition must start with a failing unit test to prove its existence and verify correctness.
3. **Execute (Consensus & Log):**
   - Delegate the sub-tasks to the appropriate tools or specialized subagents.
   - Update `CLAUDE.md` before concluding the session to record newly added dependencies, build instructions, or environment changes.

## Design Rules & Guidelines

### Interactive-Clarify Protocol
- Limit clarification questions to at most 3 to respect user flow.
- Format questions cleanly. Do not "vibe-code" or make assumptions on database, API schema, or frameworks.

### Code Quality and Review Gates
- All developed work must pass the code-review gate before merge.
- Track completed tasks visually via checklist items.

## Example Implementation Checklist
Copy and use this checklist on every orchestrator turnaround:

- [ ] Engage user with clarification questions (if ambiguity exists).
- [ ] Determine the routing path of skills (e.g., product-spec -> system-design -> feature-dev -> review).
- [ ] Establish TDD strategy and write a failing test first.
- [ ] Check performance, clean architecture, and security boundaries.
- [ ] Run reviews and validation checks.
- [ ] Update `CLAUDE.md` with new features, setup instructions, or build commands.
