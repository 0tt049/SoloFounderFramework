# Permissions: SoloFounderFramework

## Context & Roles
The SoloFounderFramework operates within a local AI agent environment (Antigravity 2.0). There is no traditional web-based Role-Based Access Control (RBAC), multi-tenancy, or OAuth tokens. 

The primary "Roles" are:
1. **Human Operator (PM / Developer)**: Has root control over the machine, approves plans, invokes slash commands.
2. **AI Agent (Antigravity)**: Operates on behalf of the Human Operator.

## Resource Access Matrix

| Resource | Operation | Actor | Enforcement Mechanism |
|----------|-----------|-------|-----------------------|
| `/brain/` (Knowledge Base) | Read/Write | AI Agent | Implicit via `brain_*` and `product_*` skills; bound by `AGENTS.md` context limits. |
| Source Code (`src/`, etc.) | Read/Write | AI Agent | Bound by explicit user approval of implementation plans (`eng_*` skills). |
| Native Tools (Filesystem, Terminal) | Execute | AI Agent | Tool permissions managed by Antigravity runtime; modifying bash commands often require human approval. |
| Configuration (`AGENTS.md`) | Write | Human / AI Agent | Agent writes only if explicitly told; PM maintains ultimate control over strategy definitions. |

## Guardrails
- **Row-Level Security (RLS)**: Not applicable (local filesystem based).
- **Code-Enforced Checks**: 
  - `Autonomy mode` setting in `AGENTS.md` ("act and tell" vs. "propose and wait") dictates whether the agent modifies files directly or drafts proposed changes.
  - Engineering skills enforce `RequestFeedback: true` on implementation plans, creating a hard stop until human approval.
