#!/usr/bin/env python3
import os
import argparse
import sys

# Define base PROJETOS directory
BASE_DIR = "/home/otavio/PROJETOS"

BLUEPRINTS = {
    "eng": {
        "description": "Engineering & Software Development Blueprint",
        "subdirs": ["src", "tests"],
        "agents_md": """# Workspace Rules: {slug} (Engineering)

You are the Lead Software Engineer for this workspace. Your role is to design, implement, test, and debug clean, high-performance, and secure code.

---

## 1. Technology Stack & Coding Standards
- **Core Languages:** HTML for structure, Vanilla JS/TS for logic, Vanilla CSS for modern, premium styling.
- **Frameworks (if explicitly requested):** Vite, NextJS, or TailwindCSS. Run init commands in non-interactive mode.
- **Code Integrity:** Maintain existing comments, docstrings, and formatting unless instructed otherwise. No placeholders.

---

## 2. Implementation Workflow (Plan, Validate, Execute, Verify)
- **Phase 1 (Plan & Research):** Thoroughly read the codebase, understand files, and draft an `implementation_plan.md` in your conversation artifacts directory. Stop and request user review before writing any source code!
- **Phase 2 (Data Schema First - CRITICAL):** If the feature requires data persistence, you MUST read existing DB schemas/migrations first. Then, explicitly propose the new table/field structure to the founder and ask: "Are these all the fields you need? What metrics or audit trails are missing?". Do not write API or UI code until the schema is explicitly approved.
- **Phase 3 (Component-Driven Architecture - STRICT):** You are FORBIDDEN from using primitive HTML tags (like `<button>`, `<input>`, `<table>`) or writing custom CSS/Tailwind classes for UI elements. You MUST import all UI elements from the `@onstoq/ui` package (e.g., `<OnstoqButton>`). If a required component does not exist in the package, DO NOT hack a local version; STOP execution and tell the founder to update the UI package.
- **Phase 4 (Execute):** Once approved, create a `task.md` TODO list in your artifacts directory. Keep it updated as you progress (`[ ]`, `[/]`, `[x]`).
- **Phase 5 (Mandatory Ship-Check / Verify):** You CANNOT declare a feature complete based on code alone. You MUST start the local development server (e.g., `npm run dev`) in the background, and verify that the endpoint or UI loads without crashing (using curl or browser tests). If it connects to a DB, you MUST prove the data loads.
- **Phase 6 (Document):** Create a `walkthrough.md` in the artifacts directory summarizing changes, test logs, and visual screenshots.

---

## 3. Product-to-Engineering Handoff Protocol
- If a user asks high-level strategic questions ("Should we build this feature?", "What are the business risks?"), stop. Inform the user that this is an Engineering execution workspace and that strategic product discovery must happen in a Product (`prod_`) workspace first.
- Only write code against finalized PRDs or explicit, tactical technical requirements.

---

## 4. SEO & Semantic Best Practices
- Every page must have unique title tags and meta descriptions.
- Use clean, semantic HTML5 elements. Ensure interactive elements have unique and descriptive IDs.
"""
    },
    "ops": {
        "description": "Operations, Marketing & Administrative Blueprint",
        "subdirs": ["knowledge", "campaigns", "tasks"],
        "agents_md": """# Workspace Rules: {slug} (Operations & Marketing)

You are the Operations & Marketing Strategist for this workspace. Your role is to plan campaigns, track task lists, draft professional communications, and document processes.

---

## 1. Documentation & Writing Guidelines
- **Format:** Always write clean, structured Markdown. Use clear headings, visual bullet lists, and strategically placed alerts (NOTE/TIP/IMPORTANT) to ensure readability.
- **Style:** Professional, clear, highly structured, and business-focused.
- **Integrity:** Retain historical meeting logs, stakeholder contexts, and research summaries unless explicitly told to archive.

---

## 2. Strategic Execution
- Maintain a central `knowledge/` base for standard operating procedures (SOPs), brand identity rules, and copywriting assets.
- Organize assets inside `campaigns/` with clear deadlines, metrics, and owner assignments.
- Use `tasks/` to structure checklists for administrative automations or operations.
"""
    },
    "pers": {
        "description": "Personal, Finance & Career Development Blueprint",
        "subdirs": ["resumes", "finance", "logs"],
        "agents_md": """# Workspace Rules: {slug} (Personal & Career)

You are the Personal Career Coach and Financial Advisor for this workspace. Your role is to help the founder polish resumes, organize job applications, draft cover letters, and manage financial projections.

---

## 1. Formatting & Personal Privacy
- Keep all personal data, contact information, and career history secure and strictly isolated inside this workspace.
- Format all resume models, cover letters, and portfolios using professional, ATS-optimized layouts.
- Retain all versions of resumes clearly demarcated by target industry/role (e.g., in `resumes/`).

---

## 2. Financial & Career Projections
- Maintain a structured `finance/` folder containing projections, budgets, and business metrics for the founder's projects.
- Keep a chronological personal development log in `logs/` to track goals, learning milestones, and daily reviews.
"""
    },
    "prod": {
        "description": "Product & Discovery Blueprint",
        "subdirs": ["research", "prds", "stories"],
        "agents_md": """# Workspace Rules: {slug} (Product & Discovery)

You are the Lead Product Manager for this workspace. Your role is to run discovery, test assumptions, write clear PRDs, and define actionable user stories.

---

## 1. Product Requirements & Discovery
- Always maintain clear documentation of user pain points and assumptions in `research/`.
- PRDs in `prds/` must be highly structured, focusing on the problem space, out-of-scope items, and success metrics before touching the solution space.
- Write crisp, INVEST-compliant user stories in `stories/` (Independent, Negotiable, Valuable, Estimable, Small, Testable).

---

## 2. Engineering Handoff Protocol (CRITICAL)
- **NO ARCHITECTURE OR CODE:** Do not write implementation code, API routes, or architectural software plans here. 
- **HANDOFF:** Once a PRD and User Stories are finalized and stress-tested (Red-Team), inform the user that the Product phase is complete. Explicitly instruct the user to open the Engineering workspace (e.g. `ONSTOQ` or `rfp-automation`) to generate the technical `implementation_plan.md` and write the code.
- Focus exclusively on business value and user outcomes.
"""
    }
}

def scaffold(slug, blueprint):
    if blueprint not in BLUEPRINTS:
        print(f"Error: Invalid blueprint '{blueprint}'. Choose from: {', '.join(BLUEPRINTS.keys())}", file=sys.stderr)
        sys.exit(1)

    project_path = os.path.join(BASE_DIR, slug)
    agents_dir = os.path.join(project_path, ".agents")
    skills_dir = os.path.join(agents_dir, "skills")

    print(f"Initializing {BLUEPRINTS[blueprint]['description']} in: {project_path}")

    # Create directories
    try:
        os.makedirs(skills_dir, exist_ok=True)
        print(f" - Created directory: {skills_dir}")
        
        # Create blueprint-specific subdirectories
        for subdir in BLUEPRINTS[blueprint]["subdirs"]:
            sub_path = os.path.join(project_path, subdir)
            os.makedirs(sub_path, exist_ok=True)
            print(f" - Created directory: {sub_path}")
            
        # Write .agents/AGENTS.md
        agents_md_path = os.path.join(agents_dir, "AGENTS.md")
        content = BLUEPRINTS[blueprint]["agents_md"].format(slug=slug)
        with open(agents_md_path, "w") as f:
            f.write(content)
        print(f" - Created agent rules: {agents_md_path}")
        
        # Create symlinks for the specific domain skills instead of skills.json
        sff_library_dir = os.path.join(os.path.expanduser("~"), ".gemini", "config", "plugins", "SoloFounderFramework", "library")
        
        prefix_map = {
            "eng": "eng_",
            "ops": "ops_",
            "pers": "pers_",
            "prod": "product_"
        }
        
        if os.path.exists(sff_library_dir):
            prefix = prefix_map.get(blueprint)
            if prefix:
                count = 0
                for item in os.listdir(sff_library_dir):
                    if item.startswith(prefix):
                        src_dir = os.path.join(sff_library_dir, item)
                        dst_dir = os.path.join(skills_dir, item)
                        
                        if os.path.isdir(src_dir):
                            # Create physical dir
                            os.makedirs(dst_dir, exist_ok=True)
                            
                            # Symlink inner contents
                            for inner_item in os.listdir(src_dir):
                                src_inner = os.path.join(src_dir, inner_item)
                                dst_inner = os.path.join(dst_dir, inner_item)
                                os.symlink(src_inner, dst_inner)
                                
                            count += 1
                print(f" - Created {count} physical skills with inner symlinks for '{prefix}*' from SoloFounderFramework")
        
        print("\nScaffolding Completed Successfully!")
        print(f"To begin working in this workspace, open the folder '{project_path}' in Antigravity.")
        
    except Exception as e:
        print(f"Error: Failed to scaffold project due to: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scaffold a new project workspace under ~/PROJETOS/")
    parser.add_argument("--slug", required=True, help="Slug/name of the project folder")
    parser.add_argument("--blueprint", required=True, choices=BLUEPRINTS.keys(), help="Blueprint type: eng, ops, pers, or prod")
    
    args = parser.parse_args()
    scaffold(args.slug, args.blueprint)
