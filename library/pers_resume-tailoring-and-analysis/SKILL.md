---
name: resume-tailoring-and-analysis
description: Tailors resumes and CVs to target job descriptions with extreme precision, leveraging a strict Truthfulness Contract to audit and restructure achievements, optimizing cover letters, conducting deep skills gap analysis, preparing specialized STAR-method interview prep, and compiling pixel-perfect PDFs using LaTeX / Tectonic.
allowed-tools: [Read, Write, Edit, Glob]
---

# Resume Tailoring and Analysis

## Goal
To audit, optimize, and tailor resumes and CVs to target job descriptions (JD), maximizing ATS keyword compatibility while strictly preserving candidate-specific real-world truthfulness, conducting deep semantic skills gap analysis, preparing comprehensive behavioral/technical interview prep, and compiling pixel-perfect outputs using LaTeX/Tectonic.

## When to Use This Skill
- When aligning an existing "master" resume to a specific job listing to highlight relevant skills.
- When performing keyword audits and semantic overlap reviews to map candidate experiences to job description prerequisites.
- When drafting clear, metric-driven achievements using action-oriented phrasing (Google X-Y-Z formula).
- When generating tailored cover letters (250–400 words) matching a specific JD.
- When conducting a comprehensive Skills Gap Analysis for a target role.
- When generating high-conversion interview preparation guides (Likely questions, STAR-method stories, and pre-interview checklists).
- When compiling LaTeX (.tex) templates into pristine 1-page PDF resumes.

### Do Not Use This Skill For:
- Automated batch scraping of multiple companies (use `automated-career-operations` instead).

## Plan-Validate-Execute Workflow

### 1. Plan (Analyze Master & Target JD)
- **Gather Inputs**: Read candidate's master resume data, target job description, optional LinkedIn profile, and personal **Experience Bank** (`experience_bank.md`).
- **Analyze Job Posting**:
  - Extract required qualifications, preferred skills, years of experience, direct tools, and methodologies.
  - Extract crucial keywords (industry terms, action verbs, company values, and specific ATS keywords).
  - Select appropriate task type: Resume Tailoring, Cover Letter Generation, Interview Preparation, Skills Gap Analysis, or comprehensive Application Strategy.

### 2. Validate (Establish Truthfulness Guardrails)
- **Truthfulness Contract**: Under no circumstances invent metrics, expand job responsibilities, alter employment dates, or falsify titles.
- **Syntactic Inspection**: If LaTeX compilation is required, ensure LaTeX syntax is intact and valid before running compilation.

### 3. Execute (Audit & Optimize)
- **Skills Gap Analysis**: Contrast job bullet points with candidate history to identify major critical gaps of tools or experience as clear, action-oriented bullet points.
- **Variant Selection**: Do not create generic, AI-stuffed bullet points; pull and arrange from verified **real experience variants** in the candidate's `experience_bank.md` that map directly to target requirements.
- **X-Y-Z Formatting**: Revise resume bullet points using the Google X-Y-Z formula: *"Accomplished [X] as measured by [Y], by doing [Z]"* where data allows. Flag missing metric values beautifully with placeholder tags: `[Metric Needed]`.
- **LaTeX Compilation**: Generate the `tailored_cv.tex` file and compile it using the Tectonic typesetting engine to verify layout alignment:
  ```bash
  tectonic tailored_cv.tex
  ```
- **Cover Letter Generation**: Produce a customized, concise cover letter (250-400 words) opening with a strong position hook, matching 2-3 key requirements with metrics, including company research, and closing with a clear CTA.
- **Interview Prep Suite**:
  - **Behavioral Questions**: Generate likely STAR-method questions based on the JD (Situation, Task, Action, Result) and help formulate stories.
  - **Technical Questions**: Compile likely technical/scenario-based questions and deep-dive topics.
  - **Interviewer Q&A**: Draft 3-5 thoughtful, high-leverage questions to ask the interviewer.
  - **Pre-Interview Checklist**: Provide a structured readiness check.

### 4. Learn & Backport
- Incorporate interview feedback, recruiter input, or custom structural changes made during job submissions directly back into the candidate's master `experience_bank.md` and local memory rules for future applications.

## Design Rules & Guidelines

### The Truthfulness Contract
- No fabrication of metrics or achievements. If a metric is missing, use placeholders: `[X]% / $[Y]` and flag them for candidate input.
- Keep structural alignment. Keep resume dates, locations, and hiring hierarchies exactly identical to the master document.

### Achievement Formatting Rules
- Start every achievement bullet with an active verb (e.g., *Formulated*, *Directed*, *Pioneered*, *Optimized*).
- Use metric-centric syntax: Lead with the result, explain the metric/measurement, and finish with the execution details.

### LaTeX and Output Rules
- Ensure the output strictly respects a single-page limit unless explicitly directed otherwise.
- Ensure all LaTeX control sequences are properly closed to avoid compilation failures under Tectonic.

## Example Implementation Checklist
Copy this checklist during Job Application optimization tasks:

- [ ] Audit the target JD to list essential keywords and technical hard skills.
- [ ] Read the master resume and select matching bullet points from the `experience_bank.md`.
- [ ] Map the candidate's master experience points directly to target JD needs.
- [ ] Conduct a detailed **Skills Gap Analysis** listing missing requirements and keywords.
- [ ] Rewrite and optimize matching resume bullets using action-packed verbs and the X-Y-Z layout.
- [ ] Draft a concise, tailored cover letter (250–400 words) aligning achievements to job prerequisites.
- [ ] Generate an **Interview Prep Guide** with STAR-method behavioral and technical questions.
- [ ] Validate and compile the LaTeX template to PDF using `tectonic tailored_cv.tex`.
- [ ] Flag missing metric values beautifully with `[Metric Needed]` or direct user questions.
- [ ] Do not invent achievements; prompt the user for additional details if required.
- [ ] Backport approved modifications or feedback into the candidate's master `experience_bank.md`.
