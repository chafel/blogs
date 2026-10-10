# Knowledge Library Implementation Plan

> Use subagent-driven-development for scoped catalog research and review.

**Goal:** Add a browsable Chinese directory of laws, models, effects and practical methods, then run the existing blog locally for review.

**Architecture:** Hugo renders a standalone directory from a versioned JSON catalog. Lightweight local CSS/JS adds search, type filtering and category navigation; entries with no article URL remain plain text. Existing theme changes are preserved.

**Tech Stack:** Existing Hugo site, JSON, HTML, CSS, vanilla JavaScript.

**Scope decision:** Implement one feature: a knowledge directory with discovery controls and optional article links. Value score (8+5+5)/(3+3+1)=2.57. No existing backlog. Daily publishing and long-form articles are outside this requested iteration.

## Task 1: Research and catalog
- Create `data/knowledge.json`: categories with stable IDs, names, descriptions; items with stable ID, Chinese name, English name, aliases, type, one-line description, optional article URL and reference sources.
- Cover practical methods including PDCA, engineering, probability, investment, cognition, systems, management, strategy, communication and learning.
- Keep uncertain or debated concepts qualified; do not claim this finite directory exhausts all knowledge.
- Validate unique IDs, required fields, category membership and URL shape.

## Task 2: Directory page
- Create `content/knowledge/_index.md`, `layouts/knowledge/list.html`, `static/css/knowledge.css`, `static/js/knowledge.js`.
- Add a navigation entry in `config.toml`.
- Use an editorial layout with sticky category navigation, search, knowledge-type selection, result counts and clear empty state.
- Retain usable category links and all content without JavaScript; support mobile, keyboard focus, reduced motion.
- Article links come from the data, never placeholder links.

## Task 3: Verify and preview
- Build with a compatible Hugo version into a temporary directory so tracked `public` files remain untouched.
- Validate rendered catalog and internal article links, search, combined filters, empty/reset state, category anchors and narrow viewport.
- Inspect a real browser screenshot and console. Use behavior checks rather than implementation-mirroring unit tests for this reversible content/UI change.
- Start local Hugo server, open `/knowledge/` and leave the server running for user review.

## Editing articles later
Populate an item's `url` with its local article URL or an external HTTPS document URL. Empty `url` displays “待撰写”. Sources are provenance references, distinct from article links.

## Completed verification
- Catalog: 184 unique entries, 10 categories, 7 types (including a distinct 定理 type), 23 discovery/reference sources.
- Hugo Extended 0.108.0 builds the complete blog successfully. Separate fixture build verifies optional internal/external article links, publication count and valid anchors without changing catalog URLs.
- Real browser checks at 1440px and 390px: PDCA and alias search, combined type filters, empty/reset state, article-only filter, category jump, Escape reset, no horizontal overflow, no console warnings/errors.
- Review resolved secondary-text contrast and clarified the Eisenhower matrix name. Local preview remains running at `http://localhost:1313/knowledge/`.
