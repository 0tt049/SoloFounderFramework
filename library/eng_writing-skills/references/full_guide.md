# Full Guide for eng_writing-skills


# Writing Skills

## Overview

**Writing skills IS Test-Driven Development applied to process documentation.**

You write test cases (pressure scenarios with subagents), watch them fail (baseline behavior), write the skill (documentation), watch tests pass (agents comply), and refactor (close loopholes).

**Core principle:** If you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing.

## Detailed Guidelines

To keep this context small, detailed instructions are split into specific guides. **You MUST use `view_file` to read the following reference files based on your current task:**

- [TDD Mapping and Skill Types](file:///home/otavio/.gemini/config/plugins/SoloFounderFramework/library/eng_writing-skills/references/tdd_mapping.md) - For understanding when to create a skill and how it maps to TDD concepts.
- [Search Optimization](file:///home/otavio/.gemini/config/plugins/SoloFounderFramework/library/eng_writing-skills/references/search_optimization.md) - **CRITICAL** for writing the Description field, selecting keywords, and ensuring token efficiency.
- [Writing Guidelines](file:///home/otavio/.gemini/config/plugins/SoloFounderFramework/library/eng_writing-skills/references/writing_guidelines.md) - For structure formatting, flowchart rules, code example guidelines, and anti-patterns.
- [Testing Methodology](file:///home/otavio/.gemini/config/plugins/SoloFounderFramework/library/eng_writing-skills/references/testing_methodology.md) - For the RED-GREEN-REFACTOR cycle, how to micro-test wordings, and how to bulletproof skills against agent rationalizations.

## Skill Creation Checklist (Quick Reference)

**RED Phase - Write Failing Test:**
- [ ] Create pressure scenarios (3+ combined pressures for discipline skills)
- [ ] Run scenarios WITHOUT skill - document baseline behavior verbatim
- [ ] Identify patterns in rationalizations/failures

**GREEN Phase - Write Minimal Skill:**
- [ ] Name uses only letters, numbers, hyphens (no parentheses/special chars)
- [ ] YAML frontmatter with required `name` and `description` fields
- [ ] Description starts with "Use when..." and includes specific triggers/symptoms
- [ ] Address specific baseline failures identified in RED

**REFACTOR Phase - Close Loopholes:**
- [ ] Add explicit counters to new rationalizations
- [ ] Re-test until bulletproof

**Deployment:**
- [ ] Commit skill to git and push.
