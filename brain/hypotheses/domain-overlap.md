# Hypotheses — Domain Overlap Between Skills

<!-- Paths in this file are relative to THIS file's location (hypotheses/<slug>.md). -->

## Meta
- Feature: `../knowledge/product/features/framework-architecture.md`
- Status: active
- Created: 2026-06-29
- Last updated: 2026-06-29

## Value risk
### H-V1: Strict domain boundaries (Brain/Product/Eng) prevent the agent from chaining skills efficiently
- **Origin:** proactive
- **Confidence:** medium
- **Evidence for:**
  - In a Solo Founder context, the transition between Product (discovery) and Engineering (execution) is fluid; forcing strict domain boundaries might stop the agent from naturally transitioning from a `product_` skill to an `eng_` skill `(intuition, PM, 2026-06-29)`
- **Evidence against:**
  - _(none yet)_
- **Open questions / caveats:**
  - Does the current architecture actually prevent cross-domain invocation, or is it just a naming convention?
- **Test:** Request a task that spans from idea validation directly to test-driven implementation in one prompt and observe if the agent artificially halts at the domain boundary.
- **Decision trigger:** If the agent refuses to cross domains without explicit permission, we need to create cross-domain workflows or soften the boundaries.
- **Status:** archived
- **Resolution:** Resolved. We decided to keep the boundaries strict because they enforce discipline (see decisions/2026-06-29-retain-namespaces.md).

## Usability risk
### H-U1: The domain prefixes (brain_, product_, eng_) are redundant cognitive overhead for a Solo Founder
- **Origin:** data-derived (from user observation)
- **Confidence:** high
- **Evidence for:**
  - The user explicitly raised concerns about "domain overlap" and previously noted that "PMs and Engineers are confused about which namespace to use" (see previous skills-overlap decision) `(chat, no artifact)`
- **Evidence against:**
  - The prefixes act as crucial context-switching triggers for the LLM to adopt the correct persona `(industry-knowledge)`
- **Open questions / caveats:**
  - Are the prefixes for the *user* to read, or for the *agent* to trigger its own state? If they are for the agent, the user shouldn't need to memorize them.
- **Test:** Remove prefixes from slash commands exposed to the user (e.g., `/brainstorm` instead of `/product_brainstorm`) while keeping them in the underlying skill filenames.
- **Decision trigger:** If usability improves without degrading agent performance, decouple user-facing commands from agent-facing skill namespaces.
- **Status:** archived
- **Resolution:** Invalidated. The PM explicitly prefers retaining the namespaces to force structured context switching.

## Feasibility risk
### H-F1: The AI agent struggles to separate "Product Thinking" from "Engineering Execution" when both domains are present in context
- **Origin:** proactive
- **Confidence:** medium
- **Evidence for:**
  - Language models tend to blend instructions when multiple distinct personas (PM, Engineer) are loaded into the same context window `(industry-knowledge)`
- **Evidence against:**
  - The recent addition of explicit `[TEXT GENERATION]` vs `[CODE EXECUTION]` metadata tags helps the agent distinguish the tools `(chat, no artifact)`
- **Open questions / caveats:**
  - Do we need to spawn separate subagents (e.g., a "Product Subagent" and an "Engineering Subagent") to truly isolate the domains?
- **Test:** Run a complex feature request in a single context vs. dispatching it to domain-specific subagents, comparing output quality and adherence to framework rules.
- **Decision trigger:** If single-context output is degraded, enforce domain isolation via subagents.
- **Status:** archived
- **Resolution:** Addressed via the explicit [METADATA] tags in the SKILL.md descriptions which successfully prevent context bleed.

## Viability risk
### H-B1: Maintaining separate domains creates artificial silos that slow down framework development
- **Origin:** proactive
- **Confidence:** low
- **Evidence for:**
  - Maintaining separate `_SCHEMA.md` and rule sets for different domains increases the maintenance burden of the SoloFounderFramework `(intuition, PM, 2026-06-29)`
- **Evidence against:**
  - _(none yet)_
- **Open questions / caveats:**
  - How much of the framework's core logic (e.g., artifact generation, routing) is duplicated across domains?
- **Test:** Audit the framework's internal tools for cross-domain duplication.
- **Decision trigger:** If core utilities are duplicated, extract them into a shared `core_` or `util_` domain.
- **Status:** archived
- **Resolution:** Invalidated. Domains serve different fundamental purposes (State Routing vs Compute Layer), so duplication is minimal.

## Other risk (Epistemic risk)
### H-O1: The "Brain" domain overlaps with the "Product" domain in knowledge management, creating dual sources of truth
- **Origin:** data-derived (from user observation)
- **Confidence:** medium
- **Evidence for:**
  - The user pointed out that `brain_` workflows (like hypothesize and decide) feel like they belong in the `product_` domain `(chat, no artifact)`
- **Evidence against:**
  - The `brain_` domain was designed as the central nervous system (state routing), while `product_` is generative.
- **Open questions / caveats:**
  - Should `brain_` just be folded into `product_`, treating product strategy as the ultimate source of truth?
- **Test:** Map all `brain_` write actions. If 100% of them write to `knowledge/product/`, then `brain_` is just a subset of `product_`.
- **Decision trigger:** If `brain_` exclusively manages product state, merge the `brain_` domain into the `product_` domain.
- **Status:** archived
- **Resolution:** Invalidated/Reframed. Mapping the write paths shows that 100% of `brain_` tools write to folders inside the `brain/` directory (`hypotheses/`, `decisions/`, `knowledge/`, `ingestion/`). The `brain/` folder *is* the Product Knowledge Base. Therefore, `brain_` is the database interface (state manager), while `product_` contains the generative functions (ideation, text generation). They do not overlap; they are the Storage Layer and the Compute Layer of the same domain.
