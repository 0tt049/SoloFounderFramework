---
name: modeling-saas-unit-economics
description: Models core SaaS unit economics, including LTV (Lifetime Value), CAC (Customer Acquisition Cost), payback periods, and cohort churn. Formulates clean charts and projections for solo founders to present to VCs.
allowed-tools: [Read, Write, Edit, Glob]
---

# Modeling SaaS Unit Economics

## Goal
To model and project critical enterprise B2B and B2C SaaS financial metrics, enabling solo founders to understand their cash position, customer economics, and unit efficiency before expanding growth spend.

## When to Use This Skill
- When calculating unit parameters: LTV, CAC, CAC payback period, and MRR churn rates.
- When organizing Cohort Retention analysis (specifically, Net Revenue Retention - NRR and Gross Revenue Retention - GRR).
- When preparing funding pitch deck financial appendices or slides.

### Do Not Use This Skill For:
- Writing full balance sheets or conducting corporate tax filings.

## Plan-Validate-Execute Workflow
1. **Plan (Identify Baseline Parameters):**
   - Gather basic metrics: MRR (Monthly Recurring Revenue), total active customers, monthly marketing ad spend, new sign-ups, and subscription tier pricing.
2. **Validate (Assess Metric Coherency):**
   - Ensure the formula constraints are mathematically flawless:
     - $CAC = \frac{\text{Total Acquisition Spend}}{\text{New Customers Acquired}}$
     - $LTV = \frac{\text{ARPU} \times \text{Gross Margin \%}}{\text{Revenue Churn Rate}}$
     - $Payback\ Period = \frac{CAC}{\text{ARPU} \times \text{Gross Margin \%}}$
   - Check if the churn rates are reasonable (e.g., alert the founder if monthly churn is $> 5\%$, representing leaky-bucket risk).
3. **Execute (Render Projections & Recommendations):**
   - Output structured, easily readable tables representing cohort retention over 6-12 months.
   - Summarize the unit efficiency indexes: LTV/CAC ratio (optimal $>3\times$), CAC payback timeline (optimal $<12\text{ months}$), and Magic Number.

## Design Rules & Guidelines

### The SaaS Growth Guardrail Rules
- **LTV/CAC Assessment**: Label ratios under $2\times$ as [CRITICAL - UNHEALTHY ECONOMICS] and advise pausing paid ads.
- **Payback Period**: Alert if customer recoup times exceed 18 months.

### Presentation Format Rules
- Projections should be rendered in clean, copy-pasteable Markdown tables.
- Clearly differentiate between booked cash flow (billings) and recognized GAAP revenue.

## Example Implementation Checklist
Copy this checklist during Finance modeling tasks:

- [ ] Assemble MRR, subscriber additions, churn counts, and total growth channel costs.
- [ ] Compute CAC, ARPU (Average Revenue Per User), and blended CAC payback period.
- [ ] Determine the current LTV/CAC health ratio.
- [ ] Create a Markdown table for Cohort Month-over-Month retention behavior.
- [ ] Check if churn exceeds standard industry caps and offer recommendations to fix retention holes.
- [ ] Format outputs with clean mathematical formulas and definitions.
