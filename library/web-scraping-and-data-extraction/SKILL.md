---
name: web-scraping-and-data-extraction
description: High-performance web scraping, crawling, and structured data extraction utilizing Firecrawl, supporting JSON-schema extraction, full-documentation crawls, screenshot captures, and stealthy bypass configurations.
allowed-tools: [Read, Write, Edit, Glob]
---

# Web Scraping and Data Extraction

## Goal
To perform highly structured, resilient, and accurate web scraping, crawling, and data extraction from websites. It enables the founder to extract clean, LLM-ready markdown, run targeted scrapes for product pages, automatically crawl entire document suites to ingest knowledge, and capture screenshots.

## When to Use This Skill
- When retrieving clean markdown or text content from a specific URL.
- When crawling a documentation portal (up to 30-50 pages) to learn a new framework or technology.
- When performing structured data extraction (e.g., product details, prices, or team lists) using a predefined JSON schema.
- When taking high-fidelity screenshots of competitive websites or designs.
- When performing live web-searches and extracting key body markdown from relevant search results.

### Do Not Use This Skill For:
- High-volume generic web scraping (thousands of pages) without an API token rate limit control.
- Bypassing strict legal walls where explicit permissions prohibit extraction (review robots.txt first).

## Plan-Validate-Execute Workflow

### 1. Plan (Analyze Request & Define Targets)
- **Identify Task Type**: Decide if the request is a single page text fetch, an entire site crawl, a structured extraction, or screenshot capture.
- **Formulate Strategy**: Determine if a static parser suffices, if a javascript-enabled crawler is required, or if stealth bypass is needed.
- **Review Schema**: If extracting structured data, design or read the target JSON schema structure.

### 2. Validate (Ensure Security & API Readiness)
- Check that `FIRECRAWL_API_KEY` is present in the environment or locally configured in the workspace's `.env` configuration.
- Check target URL accessibility and robots.txt constraints to avoid direct blocking.

### 3. Execute
- **Fetch Page Content**: Call Firecrawl API or local scripts to fetch the URL's clean markdown content:
  ```bash
  python3 scripts/fc.py fetch "<URL>"
  ```
- **Crawl Portal**: Run deep crawl for complete documentation:
  ```bash
  python3 scripts/fc.py crawl "<BASE_URL>" --limit 30
  ```
- **Extract Structured Data**: Submit target page with JSON Schema configuration to extract precise key-value fields:
  ```bash
  python3 scripts/fc.py extract "<URL>" --schema schema.json
  ```
- **Capture Screenshots**: Capture and save layout PNG outputs for design analysis:
  ```bash
  python3 scripts/fc.py screenshot "<URL>" -o layout.png
  ```

### 4. Clean & Refine
- Audit output results for incomplete rendering, bot-detection blocks (e.g., Cloudflare gate pages), or malformed JSON data.
- Save the structured JSON outputs or clean markdown docs directly to the workspace's `brain_data` or relative directories for use.

## Design Rules & Guidelines

### API Key and Integration Rule
- Always use environment variables for `FIRECRAWL_API_KEY` rather than hardcoding.

### Stealth and Compliance
- Always introduce mild random delay cycles between deep crawling operations to mimic human navigation and prevent prompt blocking.
- Avoid hammering endpoints simultaneously; use polite sequential crawling.

---

## Example Implementation Checklist
Copy this checklist during Web Scraping & Data Extraction tasks:

- [ ] Check if `FIRECRAWL_API_KEY` is active and configured in the environment.
- [ ] Determine if the target is a single-page scrape, structured field extraction, or documentation deep crawl.
- [ ] Write schema.json if a structured data extraction is requested.
- [ ] Execute target fetching script or command.
- [ ] Verify if the output got blocked by Cloudflare. If blocked, adjust stealth headers/fetcher parameters if applicable.
- [ ] Parse extracted data or compile the crawled markdown pages.
- [ ] Format outputs in neat, reader-friendly tables or markdown files inside the workspace.
