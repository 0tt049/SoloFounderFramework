# Test Coverage: SoloFounderFramework

| Use case | Rule (doc) | Expected behavior (+ deny case) | Evidence | Type | Status |
|----------|-----------|---------------------------------|----------|------|--------|
| Planning Gate | `flows.md`: Implementation Planning Flow | The agent MUST set `ArtifactMetadata.RequestFeedback: true` when generating an `implementation_plan.md`. If false, execution is halted/flagged. | `flows.md`, `permissions.md` | integration | proposed |
| Execution Gate | `permissions.md`: Resource Access | The agent MUST NOT modify source code files before the Human Operator approves the implementation plan. | `permissions.md`, `automation.md` | integration | proposed |
| Brain Provenance | `automation.md`: Brain Processing | Ingested insights MUST contain a valid link to a raw `source/` file. If missing, the ingestion is rejected. | `automation.md` | integration | proposed |


### Existing coverage
*(No automated tests exist in the repository today. All rules are currently unverified gaps.)*

### Proposed tests

#### Flow & Permission Rules
- **Enforce Implementation Plan Gate**
  - *Assert:* A mock agent tool-call payload writing to `implementation_plan.md` with `RequestFeedback: false` fails the internal framework validation check.
  - *Type:* integration (deterministic)
- **Provenance Link Validator**
  - *Assert:* A generated insight string without a `[source/...]` tag throws a validation error during the `brain_ingest` workflow.
  - *Type:* unit



### Gaps — documented but unverified
1. **Implementation Plan Approval Gate (High Risk):** An agent could theoretically bypass the `RequestFeedback` flag if the Antigravity runtime validation changes, leading to unapproved code execution.
2. **Provenance Validation (Medium Risk):** Without a strict checker, the agent might start synthesizing insights without sources, slowly drifting the knowledge base into hallucination.
