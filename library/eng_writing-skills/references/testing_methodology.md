# Skill Testing Methodology

## The Iron Law

```
NO SKILL WITHOUT A FAILING TEST FIRST
```

Write skill before testing? Delete it. Start over.
Edit skill without testing? Same violation.

**No exceptions:**
- Not for "simple additions"
- Not for "just adding a section"
- Don't keep untested changes as "reference"

## RED-GREEN-REFACTOR for Skills

### RED: Write Failing Test (Baseline)
Run pressure scenario with subagent WITHOUT the skill. Document exact behavior:
- What choices did they make?
- What rationalizations did they use?

### GREEN: Write Minimal Skill
Write skill that addresses those specific rationalizations. Don't add extra content for hypothetical cases. Verify agents now comply.

### REFACTOR: Close Loopholes
Agent found new rationalization? Add explicit counter. Re-test until bulletproof.

## Match the Form to the Failure

When writing skill instructions, choose the structural form that directly addresses the observed agent failure:

| Baseline failure | Right form | Wrong form |
|---|---|---|
| Skips/violates a rule under pressure | Prohibition + rationalization table + red flags | Soft guidance ("prefer...", "consider...") |
| Wrong output shape | Positive recipe/contract | Prohibition list ("don't restate") |
| Omits a required element | Structural REQUIRED field in template | Prose reminders near template |
| Conditional behavior | Conditional keyed to observable predicate | Unconditional rule + exemption clauses |

## Micro-Test Wording Method

1. **One fresh-context sample per call**: Run each test in a fresh conversation.
2. **Always include a no-guidance control**: Test without the skill active.
3. **5+ reps per variant**: Run at least 5 independent repetitions.
4. **Manually read every flagged match**: Read the agent's reasoning.
5. **Variance is a metric**: If wording fails 2 out of 5, keep refining.

## Bulletproofing Skills Against Rationalization

- **Close Every Loophole Explicitly**: Don't just state the rule - forbid specific workarounds.
- **Address "Spirit vs Letter" Arguments**: Add foundational principles.
- **Build Rationalization Table**: Capture excuses agents make and list realities.
- **Create Red Flags List**: Make it easy for agents to self-check when rationalizing.
