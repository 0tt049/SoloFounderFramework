# Variables: SoloFounderFramework

## Configuration & Context Limits

This system does not use standard environment variables (like API keys) directly in the framework files; those are handled by the Antigravity runtime. Instead, "variables" in this context refer to the operating parameters defined in the agent's brain, specifically `AGENTS.md`.

| Configuration | Scope | Defined In | Risk / Impact |
|---------------|-------|------------|---------------|
| `Autonomy mode` | System-wide | `AGENTS.md` | **High**: Determines if the agent acts autonomously ("act and tell") or requires human confirmation ("propose and wait"). Drift here could lead to unapproved writes. |
| `Maintenance cadence` | System-wide | `AGENTS.md` | **Low**: Defines how often `/review` tasks are expected to be run (e.g., Weekly). |
| `Context budget` | Agent Runtime | `AGENTS.md` | **Medium**: Limits how many files the agent should load (e.g., `INDEX.md`, target file, + 3 adjacent files). Exceeding this risks prompt bloat and logic degradation. |
| `Evidence hierarchy` | Heuristic | `AGENTS.md` | **Medium**: Rules defining how conflicting data is weighted (Decisions > Strategy > Customer Evidence). |

## Pre-Go-Live Checklist
Since this is an AI assistant framework and not a deployed service, "go-live" occurs when the plugin is enabled in `~/.gemini/config/plugins/`.
- [ ] Confirm `plugin.json` is correctly formatted.
- [ ] Ensure the Antigravity agent has parsed `AGENTS.md`.
- [ ] Verify `Autonomy mode` aligns with the operator's comfort level.
