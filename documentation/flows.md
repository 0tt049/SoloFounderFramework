# Flows: SoloFounderFramework

## Core Journeys

### 1. Ingestion Flow (Brain)
- **Actor**: User / PM
- **Precondition**: New artifact (interview, meeting, analytics snapshot) provided via `/ingest` (now `brain_ingest`).
- **Path**: UI → Agent (`brain_ingest` skill) → `source/` (raw) → `ingestion/` (synthesized) → `knowledge/` (canonical).
- **Authz check**: Local filesystem write permissions.
- **Trust-boundary crossings**: Agent reading user input; Agent writing to local filesystem.
- **Side effects**: Creation of durable knowledge files, update of INDEXes.

### 2. Implementation Planning Flow (Engineering)
- **Actor**: Agent (Engineering subagent)
- **Precondition**: User requests a new feature or bugfix.
- **Path**: Agent (`eng_writing-plans` skill) → Reads `brain/AGENTS.md` and strategy → Generates `implementation_plan.md` → Waits for User approval.
- **Authz check**: Agent waits for explicit User approval (`ArtifactMetadata.RequestFeedback: true`).
- **Trust-boundary crossings**: Agent proposing changes; User approving changes.
- **Side effects**: Creation of `implementation_plan.md` artifact.

### 3. Execution Flow (Engineering)
- **Actor**: Agent (Engineering subagent)
- **Precondition**: Implementation plan approved.
- **Path**: Agent (`eng_executing-plans`) → Parses plan → Reads code (`view_file`, `grep_search`) → Edits code (`write_to_file`, `multi_replace_file_content`) → Verifies (`run_command`).
- **Authz check**: Implicitly granted by prior user approval of the plan.
- **Trust-boundary crossings**: Agent modifying source code; Agent executing bash commands.
- **Side effects**: Code modifications, terminal command execution.

### 4. Ship Check Flow (Product/Engineering)
- **Actor**: Agent
- **Precondition**: Implementation is complete, tests pass.
- **Path**: Agent (`product_ship-check`) → Reads recent changes → Updates documentation → Prepares PR/Merge summary.
- **Authz check**: Verifies tests pass before claiming success (`eng_verification-before-completion`).
- **Trust-boundary crossings**: Agent aggregating data across the workspace.
- **Side effects**: Final documentation updates, potential git operations.
