---
name: automated-career-operations
description: Automates multi-agent job application workflows using a high-level 8-phase orchestration pipeline, including candidate profiling, batch-scoring listings, stakeholder intelligence scanning, auto-fill mappings, and centralized tracking CRM.
allowed-tools: [Read, Write, Edit, Glob]
---

# Automated Career Operations

## Goal
To scale and automate structured career and job application operations, replacing manual tracking and vetting with high-volume, multi-agent evaluation, precise target research, and an 8-phase end-to-end pipeline.

## When to Use This Skill
- When retrieving or scanning job listings from multiple career portals (e.g., Ashby, Greenhouse, Lever, Workday).
- When assessing job opportunities against a defined personal preference profile (compensation, stack, arrangement).
- When automating outreach email drafting, cold message networking sequences, and target stakeholder research.
- When orchestrating the job hunt lifecycle across the 8-phase workflow.
- When organizing and updating the applicant CRM schema (`tracker.md`).

### Do Not Use This Skill For:
- Deep manual line-by-line CV/resume editing (use `resume-tailoring-and-analysis` instead).

## The 8-Phase Orchestration Pipeline

The career agent operates through a highly structured 8-phase state machine:

```text
Orchestrator ───────────────────────────────────────────┐
 ├─ Phase 0: Bootstrap (Master CV, Profile, Exp Bank)    │
 ├─ Phase 1: Research (Company, Hiring Manager, Salaries)│
 ├─ Phase 2: Tailor (Hand off to resume-tailor sub-skill)│
 ├─ Phase 3: Pre-submission Review (Adversarial review)  │
 ├─ Phase 4: Submission Walkthrough (Manual forms guide) │
 ├─ Phase 5: Track (Status logging in tracker.md CRM)    │
 ├─ Phase 6: Outreach (LinkedIn DMs, Cold emails to HM)  │
 └─ Phase 7: Learn & Backport (Feed learnings → memory)   │
```

## Plan-Validate-Execute Workflow

1. **Plan (Target Prefs & Weighting):**
   - Collect user's preferences: salary floor, location (remote/hybrid), technology stack, and company stage.
   - Establish the grading schema: A-F based on criteria match percentages.

2. **Validate (Portal Verification):**
   - Verify listing contents. Ensure expired postings are flagged and non-negotiable hurdles (e.g., relocation requirements) are evaluated.
   - Verify all workspace assets: `config.yaml`, `tracker.md`, and `experience_bank.md` exist and are structured properly.

3. **Execute (Process & Research):**
   - **Grading Matrix**: Produce a fitness scoring matrix comparing opportunities in a markdown table.
   - **Stakeholder Scan**: Scan LinkedIn context or target webpages to locate hiring decision-makers, internal recruiters, or mutual contacts.
   - **Form Auto-Fill**: Map the candidate's tailored JSON profile features to Greenhouse/Lever/Workday application input fields to prepare auto-fill payloads or step-by-step copy-paste submission walks.
   - **Outreach Draft**: For high-scoring targets (Grade B+), draft customized outreach pitches matching the specific contact's role.
   - **Tracker Updates**: Log all activities and application updates inside the master `tracker.md` file.

4. **Learn & Backport:**
   - At Phase 7, analyze rejection reasons or interview feedback, and append them to `memory_rules.md` to prevent similar issues and refine next cycles.

## Design Rules & Guidelines

### Grading Criteria Weights
- **Base Salary**: MUST meet the specified floor (Weight: 35%).
- **Tech Stack Match**: Essential frameworks/languages listed in the profile (Weight: 25%).
- **Work Arrangement**: Remote/Hybrid alignment (Weight: 25%).
- **Autonomy & Influence**: Role scope and leadership indicators (Weight: 15%).

### Stakeholder Engagement Tone
- Cold-reach messages must be direct, polite, concise (under 150 words), and focus strictly on mutual value rather than generic flattery.

### CRM Tracker File Schema (`tracker.md`)
Maintain a flat Markdown table with columns:
`| Company | Role | Grade | Current Phase | Applied Date | Last Contact | Status | Notes |`

## Example Implementation Checklist
Copy this checklist during Career Ops tasks:

- [ ] Define the career preference profile including salary, stack, and remote requirement.
- [ ] Parse target listings and extract location terms, stack information, and pay brackets.
- [ ] Create a comparative evaluation table utilizing letter grades (A-F).
- [ ] Perform Phase 1 Stakeholder and Hiring Manager discovery.
- [ ] Hand off the target JD to `resume-tailoring-and-analysis` for material creation.
- [ ] Construct the auto-fill payload mapping master details to Greenhouse/Workday form schemas.
- [ ] Log the application in `tracker.md` with active status.
- [ ] Draft concise, professional, and personalized outreach messages for the Hiring Manager.
- [ ] Capture phase transition feedback (e.g., recruiter notes) and execute the Phase 7 Learn sequence.
