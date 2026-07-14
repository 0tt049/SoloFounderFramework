---
name: brain_project-router
description: "Scaffold a new project workspace under ~/PROJETOS/ based on tailored domain blueprints (Engineering, Operations, Personal)."
---

# project-router workflow

## `/scaffold <slug>` or `/brain_project-router <slug>`

This skill transitions a strategic concept or feature conceived inside the `BRAIN` workspace into an executable, isolated workspace under `~/PROJETOS/<slug>`.

### 1. Semi-Automated Protocol (Approved)
Before creating any directories or writing files, the agent MUST present the proposed workspace blueprint to the founder:
1. Show the proposed `<slug>` and target directory path: `~/PROJETOS/<slug>`.
2. Present the tailored `.agents/AGENTS.md` rules and structure for the selected domain blueprint.
3. Ask the user for confirmation (using a simple "Yes/No" or "Proceed" interaction).
4. Run the scaffolding script only AFTER receiving explicit user confirmation.

### 2. Tailored Domain Blueprints

#### A. Engineering (`eng`)
*   **Target Scope:** Coding, MVC development, script automation, API integrations.
*   **Blueprint Structure:**
    - Directory: `~/PROJETOS/<slug>`
    - Customized `.agents/AGENTS.md` containing strict code review, planning, execution, and validation rules.
    - Initial folders: `src/`, `tests/`.

#### B. Operations & Marketing (`ops`)
*   **Target Scope:** Content generation, task tracking, administrative documentation, copywriting.
*   **Blueprint Structure:**
    - Directory: `~/PROJETOS/<slug>`
    - Customized `.agents/AGENTS.md` optimized for document-driven, markdown-heavy flows (no heavy coding standards).
    - Initial folders: `knowledge/`, `campaigns/`, `tasks/`.

#### C. Personal & Career (`pers`)
*   **Target Scope:** Resume polishing, job applications, financial modeling, personal goals.
*   **Blueprint Structure:**
    - Directory: `~/PROJETOS/<slug>`
    - Customized `.agents/AGENTS.md` with guidelines for CV building, matching skills to jobs, and personal logging.
    - Initial folders: `resumes/`, `finance/`, `logs/`.

#### D. Product & Discovery (`prod`)
*   **Target Scope:** Product Requirements (PRD), User Stories, Discovery, Assumption testing.
*   **Blueprint Structure:**
    - Directory: `~/PROJETOS/<slug>`
    - Customized `.agents/AGENTS.md` focused on PM workflows.
    - Initial folders: `research/`, `prds/`, `stories/`.

---

## Technical Invocation

The agent invokes the scaffolding automation by running:
`python3 /home/otavio/.gemini/config/plugins/SoloFounderFramework/library/brain_project-router/scripts/scaffold_project.py --slug <slug> --blueprint <eng|ops|pers>`
