# Decision: Retain Domain Namespaces

## Status
decided

## Date
2026-06-29

## Context
There was an ongoing discussion and hypotheses generated regarding the potential cognitive overhead of using three distinct namespaces (`brain_`, `product_`, `eng_`) for a Solo Founder. The alternative considered was to simplify user-facing commands (e.g., using `/brainstorm` instead of `/product_brainstorm`).

## Options considered
1. **Remove user-facing prefixes**: Alias all commands to remove the domains from the user's view while keeping them in the backend files.
2. **Retain explicit namespaces**: Keep `brain_`, `product_`, and `eng_` visible to the user to enforce explicit context boundaries and maintain organized drawers.

## Decision
**Retain explicit namespaces**. The PM (User) explicitly preferred keeping the namespaces. The explicit prefixes serve as an important architectural boundary that clarifies the intent of the tool being used (e.g., state routing vs. execution vs. strategy).

## Why
While a unified namespace might feel superficially simpler, explicitly declaring the domain (`eng_` vs `product_`) reinforces discipline. It forces the Solo Founder to put on the correct "hat" before executing a command, matching the framework's intent of structured context switching.

## Evidence
- Direct PM explicit preference.  (intuition, PM, 2026-06-29)

## Explicitly NOT doing
- We are not stripping domain prefixes from slash commands or skill invocations.  (intuition, PM, 2026-06-29)

## What would reverse this
If future iterations of the framework introduce a unified agent capable of automatic semantic routing without needing domain hints, the explicit prefixes might become obsolete.

## Remaining ambiguities
- None.

## Linked
- Hypotheses: `../hypotheses/domain-overlap.md`
