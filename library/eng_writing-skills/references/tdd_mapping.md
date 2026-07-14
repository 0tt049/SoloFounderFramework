# TDD Mapping and Directory Structure for Skills

## What is a Skill?

A **skill** is a reference guide for proven techniques, patterns, or tools. Skills help the agent find and apply effective approaches.

**Skills are:** Reusable techniques, patterns, tools, reference guides
**Skills are NOT:** Narratives about how you solved a problem once

## TDD Mapping for Skills

| TDD Concept | Skill Creation |
|-------------|----------------|
| **Test case** | Pressure scenario with subagent |
| **Production code** | Skill document (SKILL.md) |
| **Test fails (RED)** | Agent violates rule without skill (baseline) |
| **Test passes (GREEN)** | Agent complies with skill present |
| **Refactor** | Close loopholes while maintaining compliance |
| **Write test first** | Run baseline scenario BEFORE writing skill |
| **Watch it fail** | Document exact rationalizations agent uses |
| **Minimal code** | Write skill addressing those specific violations |
| **Watch it pass** | Verify agent now complies |
| **Refactor cycle** | Find new rationalizations → plug → re-verify |

## When to Create a Skill

**Create when:**
- Technique wasn't intuitively obvious to you
- You'd reference this again across projects
- Pattern applies broadly (not project-specific)
- Others would benefit

**Don't create for:**
- One-off solutions
- Standard practices well-documented elsewhere
- Project-specific conventions (put in GEMINI.md)
- Mechanical constraints (if it's enforceable with regex/validation, automate it)

## Skill Types

- **Technique**: Concrete method with steps to follow (condition-based-waiting, root-cause-tracing)
- **Pattern**: Way of thinking about problems (flatten-with-flags, test-invariants)
- **Reference**: API docs, syntax guides, tool documentation (office docs)

## Directory Structure

```
skills/
  skill-name/
    SKILL.md              # Main reference (required)
    references/           # Heavy reference and documentation files
    scripts/              # Executable tools
```

**Flat namespace** - all skills in one searchable namespace

**Separate files for:**
1. **Heavy reference** (100+ lines) - API docs, comprehensive syntax
2. **Reusable tools** - Scripts, utilities, templates

**Keep inline (in SKILL.md):**
- Principles and concepts
- Triggers and description
- When to read references

## File Organization

### Self-Contained Skill
```
defense-in-depth/
  SKILL.md    # Everything inline
```

### Skill with Reusable Tool
```
condition-based-waiting/
  SKILL.md    # Overview + patterns
  example.ts  # Working helpers to adapt
```

### Skill with Heavy Reference
```
pptx/
  SKILL.md       # Overview + workflows
  references/
    pptxgenjs.md # 600 lines API reference
    ooxml.md     # 500 lines XML structure
  scripts/       # Executable tools
```
