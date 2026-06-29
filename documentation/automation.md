# Automation: SoloFounderFramework

## Embedded Agents & Automated Workflows

The SoloFounderFramework essentially transforms the Antigravity Agent into an embedded, autonomous product and engineering operator. This document defines how these automated workflows are structured and constrained.

### Core Automations

#### 1. Brain Processing (`brain_*` skills)
- **Trigger**: User `/ingest` command, or conversational inputs.
- **Owner**: Antigravity Agent (Core)
- **Inputs**: User transcripts, market data, repo markdown files.
- **Tools Called**: `view_file`, `write_to_file`, `multi_replace_file_content`.
- **Steering**: Guided by `AGENTS.md` and specific `SKILL.md` prompts.
- **Hard Guardrails**: The agent must link claims to `source/` files (provenance) and cannot arbitrarily scrape the web without the `search_web` or `read_url_content` tools.
- **Approval Gates**: Generally runs automatically (if "act and tell" is enabled in `AGENTS.md`) for reversible ingestion. Modifying core strategy requires explicit PM approval.

#### 2. Engineering Execution (`eng_*` skills)
- **Trigger**: User request to build a feature.
- **Owner**: Antigravity Agent (Engineering Subagent)
- **Inputs**: Implementation plans, existing codebase.
- **Tools Called**: Full suite of native tools (`run_command`, `write_to_file`, `grep_search`, `invoke_subagent`).
- **Steering**: Guided by `eng_executing-plans` and test-driven development directives.
- **Hard Guardrails**: The agent tool surface restricts what can be run. Destructive commands (e.g., deleting a database) often require human confirmation via the terminal prompt.
- **Approval Gates**: The creation of an `implementation_plan.md` MUST use `RequestFeedback: true`, stopping automation until the human clicks "Proceed".

### Output Contract
- **App-owned side effects**: The agent writes markdown to the local filesystem and modifies source code directly.
- **Agent-owned suggestions**: Output in conversational UI (e.g., "Want me to run a security audit now?").
- **Failure Handling**: If an agent fails to execute a plan, it falls back to conversational debugging with the human operator.
