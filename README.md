# SoloFounderFramework

The SoloFounderFramework is a unified ecosystem for native operation within Antigravity 2.0. It bridges memory management, product decisions, and technical execution by agents into a single synchronous loop, eliminating friction when transitioning between roles.

## The Assembly Line

The framework's architecture was designed to operate as a relentless assembly line. Components do not merely exist side by side; they have hard dependencies on one another, ensuring fluid and mandatory execution.

- **Brain (`/brain/`)**: The central repository for project context and long-term memory. It stores architectural decisions, hypotheses, and stakeholder interactions.
- **Product (`/skills/product_*`)**: The strategists who conceive ideas, validate assumptions, build roadmaps, and conduct market research.
- **Engineering (`/skills/eng_*`)**: The software engineers focused on Test-Driven Development (TDD), architecture audits, and technical execution.

### Synchronous Workflow

The operation follows an automated handoff pipeline that integrates Memory, Strategy, and Execution:

```mermaid
graph TD
    B[Brain: /brain/decisions/] -->|Define Constraints| W[Engineering: eng_writing-plans]
    W -->|Creates implementation_plan.md| SDD[Engineering: eng_subagent-driven-development]
    SDD -->|Writes Code & Tests| FDB[Engineering: eng_finishing-a-development-branch]
    FDB -->|Invokes Architecture Audit| SC[Engineering: eng_ship-check]
    SC -->|Pass/Fail| FDB
    FDB -->|Merges| Main[Main Branch]
```

## How to Use

The single manifest `plugin.json` exposes the toolkit to the Antigravity session. Every agent entering the workspace will instinctively know:

1. That technical plans (`eng_writing-plans`) cannot be written without a prior inspection of `/brain/decisions/`.
2. That merges (`eng_finishing-a-development-branch`) are blocked and require a strict technical audit (`eng_ship-check`) before completion.
