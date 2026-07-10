---
name: three-statement-projection
description: Builds, links, and audits integrated three-statement financial projections (Income Statement, Balance Sheet, Cash Flow Statement) in Python or Excel models. Trigger this during comprehensive modeling or strategic business forecasting.
allowed-tools: [Read, Write, Edit, Glob]
---

# Three Statement Financial Projections

## Goal
To programmatically generate, link, and validate fully integrated, error-free three-statement financial models (Income Statement, Balance Sheet, Cash Flow Statement).

## When to Use This Skill
- When building comprehensive historical or project financial forecasts.
- When conducting scenario analysis (Base, Upside, Downside) using structured drivers.
- When validating statement integration to ensure models balance correctly.

### Do Not Use This Skill For:
- Simple monthly cash-burn or margin audits. Use the simpler financial analysis skill instead.
- Formal annual public audit filing or local corporate tax submission.

## Plan-Validate-Execute Workflow
1. **Plan (Scoping & Layout Design):**
   - Identify sheet layout, time period orientation (columns representing years), assumptions, and tax/interest rates.
2. **Validate (Dynamic Modeling & Recalculation):**
   - In Python (e.g. using `openpyxl`), write all formulas as dynamic string equations (e.g. `ws["D15"] = "=D14*(1+Assumptions!$B$5)"`). Avoid hardcoding derived metric valuations.
   - Run a programmatic recalculation step after cell modifications to verify integrity.
   - In Excel Office JS, assign formulas directly to `.formulas` rather than setting statics.
3. **Execute (Sequential Integration & Audit):**
   - Step 1: Input and confirm historical datasets.
   - Step 2: Build the Income Statement projection (revenue, COGS, GM, SG&A, interest, taxes, Net Income).
   - Step 3: Populate the Balance Sheet (Assets, Liabilities, Equity) making sure `Assets = Liabilities + Equity` balances precisely.
   - Step 4: Construct the Cash Flow Statement linking Net Income, adding back D&A, tracking changes in Working Capital, and validating that Ending Cash ties exactly back to Cash on the Balance Sheet.

## Design Rules & Guidelines

### Integrity Constraints (Non-Negotiable)
- All roll-forwards, net assets, and cash subtotals must exist as formulas, never as raw numbers.
- Any discrepancy where `Assets - (Liabilities + Equity) != 0` must initiate immediate recalculation troubleshooting.
- Changes in working capital assets (e.g. Inventory, Receivables) must utilize the correct sign convention (increases are negative/uses of cash).

### Scenario & Error Auditing
- Maintain scenario toggles (Base, Upside, Downside) using `=CHOOSE()` or `=INDEX()` formulas linked to assumptions.
- Proactively check for and remove common spreadsheet errors: `#REF!`, `#DIV/0!`, `#VALUE!`, and `#NAME?`.

## Example Implementation Checklist
Copy this checklist during integrated model development sessions:

- [ ] Structure columns to distinguish historical periods from projection periods.
- [ ] Connect Income Statement net earnings to the Balance Sheet's Retained Earnings.
- [ ] Ensure Net Income flows as the starting basis of the Cash Flow Statement.
- [ ] Add back Depreciation & Amortization to cash flows while subtracting it from cumulative assets on the Balance Sheet.
- [ ] Confirm that Ending Cash on the Cash Flow matches Cash on the Balance Sheet exactly.
- [ ] Perform programmatic audits for null reference/divide-by-zero errors.
- [ ] Deliver a fully balanced, formulas-dense spreadsheet.
