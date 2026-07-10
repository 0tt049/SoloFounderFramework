---
name: managing-founder-equity-and-safes
description: Evaluates and models founder equity allocation, vesting terms (such as standard 4-year/1-year cliff), and Simple Agreements for Future Equity (SAFE) notes.
allowed-tools: [Read, Write, Edit, Glob]
---

# Managing Founder Equity And SAFEs

## Goal
To model equity cap tables, split co-founder equity fairly, structure vesting agreements, and model SAFE note dilutions (pre-money and post-money SAFEs) to protect early founders during investment cycles.

## When to Use This Skill
- When designing co-founder equity splits and structuring vesting parameters.
- When drafting or reviewing standard Y-Combinator SAFE note templates (Valuation Cap and Discount).
- When simulating seed funding dilutions on early cap tables.

### Do Not Use This Skill For:
- Formal tax filing guidance or executing binding state-level corporate filings (GDPR, LLC setup, 83(b) elections) without legal counsel.

## Plan-Validate-Execute Workflow
1. **Plan (Gather Capitalization & Investment Data):**
   - Collect present shareholders: outstanding shares, option pools, co-founder contributions.
   - Collect proposed SAFE terms: valuation caps, discount rates, investment sum.
2. **Validate (Analyze Dilution Risks):**
   - Apply strict legal disclaimer: "Warning: I am an AI, not an attorney. This is not formal legal counsel."
   - Check if the option pool is pre-money or post-money, and cross-calculate cap table percentages.
3. **Execute (Render Cap Table & Dilution Projections):**
   - Present a clear cap table before and after the SAFE conversion (usually upon Series A preferred round).
   - Detail the exact dilution impact on founders and outline safe co-founder vesting schedule matrices.

## Design Rules & Guidelines

### Legal Disclaimer Obligation
- EVERY output modifying equity, caps, or SAFEs must start with:
  > [!IMPORTANT]
  > **LEGAL DISCLAIMER**: This modeling does not constitute formal legal counsel. Always consult a qualified startup attorney before executing cap table agreements or SAFEs.

### Vesting Standard Protection Guild
- Strongly advocate for a standard **4-year vesting schedule with a 1-year cliff** to protect the company from short-term co-founder attrition.

## Example Implementation Checklist
Copy this checklist during Equity/Funding tasks:

- [ ] Include the mandatory Legal Disclaimer alert prominently.
- [ ] Define the current capitalization (founders' shares, options, total pool).
- [ ] Calculate dilution under pre-money vs. post-money Valuation Cap notes.
- [ ] Structure co-founder equity splits with 4-year vesting/1-year cliff terms.
- [ ] Display comparative dilution percentages in clean Markdown tables.
- [ ] Ensure clear separation between equity ownership percentages vs. voting control.
