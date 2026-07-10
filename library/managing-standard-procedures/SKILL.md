---
name: managing-standard-procedures
description: Designs, builds, and validates company Standard Operating Procedures (SOPs) and operational runbooks using the 5W2H framework. Trigger this when document runbooks, onboarding steps, or operations processes are needed.
allowed-tools: [Read, Write, Edit, Glob]
---

# Managing Standard Operating Procedures (SOPs)

## Goal
To programmatically draft, audit, and optimize company operational runbooks and SOPs, enforcing strict accountability, success verification, and rollback paths.

## When to Use This Skill
- When designing Standard Operating Procedures (SOPs) for recurrent operational actions (e.g. employee onboarding, IT provisioning, customer support intake).
- When conducting quality audits on raw or outdated company wikis.
- When creating regulatory compliance runbooks (such as SOC2, HIPAA, or ISO controls).

### Do Not Use This Skill For:
- Interactive terminal-command execution or server debugging protocols.

## Plan-Validate-Execute Workflow
1. **Plan (5W2H Scoping):**
   - Gather critical process dimensions: **Who** (actor/role), **What** (actions), **When** (triggers), **Where** (platforms/tools), **Why** (legal/operational intent), **How** (precise steps), and **How Much** (budget/expected duration).
2. **Validate (6-Attribute Quality Check):**
   - Audit every step inside a process against the 6 Quality Pillars:
     1. *Named Operator:* A concrete role or individual (never a generic "ops team").
     2. *Expected Duration:* Time metric (e.g., "10 minutes").
     3. *Observable Success Signal:* Testable state change (e.g. "receive HTTP 200", not "verify system").
     4. *Observable Failure Signal:* Distinct error state detection.
     5. *Rollback Path:* Explicit steps to revert actions if failure occurs.
     6. *Escalation Contact:* Named person or on-call rotation.
3. **Execute (Render Standardized Runbook):**
   - Output the structured SOP incorporating the Version Control Header, RACI responsibilities matrix, chronological 5W2H playbook instructions, and escalation troubleshooting.
   - For regulated industries, append compliance overlays (GDPR, SOC2, HIPAA).

## Design Rules & Guidelines

### Operational Accountability
- Every SOP must have an assigned, active Human Owner to prevent knowledge stale-out.
- Output score: Documents failing to specify named owners or verifiable outcome signals receive a quality score of < 60/100 and must be revised immediately.

### Layout Formats
- Use standard Markdown tables for RACI matrices and parameter logs.
- Utilize clear callout blocks to highlight high-risk actions or emergency rollback directions.

## Example Implementation Checklist
Copy this checklist during SOP drafting operations:

- [ ] Select operational profile (Ops, Support, HR, Finance, Regulated).
- [ ] Map out ownership matrix using standard RACI structures.
- [ ] Implement the 5W2H workflow sequence.
- [ ] Trace each playbook stage to confirm duration, success signal, and failure indicator.
- [ ] Define the exit rollback choreography.
- [ ] Apply compliance overlays if SOC2/HIPAA is active.
- [ ] Deliver a scannable, audit-ready markdown SOP.
