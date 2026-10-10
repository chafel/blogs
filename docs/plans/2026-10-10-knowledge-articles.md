# Knowledge Articles Implementation Plan

**Goal:** Give all 184 directory entries a full, original Chinese article and a working directory link, ready for local review.

**Architecture:** Articles live at `content/knowledge/<id>.md`, served by a dedicated `layouts/knowledge/single.html` sharing the directory visual language. The catalog remains the source of category, English title, type and related-entry navigation. Only the parent updates catalog URLs and shared templates; writing agents own disjoint article IDs.

**Scope:** Existing 184 entries; no automatic daily publishing or external deployment. All articles are available for local review now. Each article has eight sections: concrete problem, one-sentence explanation, origin, mechanism, worked example, applicability and counterexamples, action, references and related entries. Target 800–1500 Chinese characters where useful; prioritize substance and exact structure over padding. Hypothetical examples must be labeled; no fabricated user experiences, quotations, origin stories or numerical claims.

## Work ownership
- Engineering + thinking + strategy: content writer A (55 articles).
- Psychology + learning + systems: content writer B (55 articles).
- Management + problem-solving: content writer C (40 articles).
- Probability + investing: parent (34 articles), plus page template and integration.

## Verification
- Each catalog entry has exactly one non-draft article with the matching ID and all eight sections.
- Article-specific primary/reliable references, explicit uncertainty where attribution or evidence is disputed, and original prose.
- Validate mathematical worked examples, link destinations, rendered headings, article navigation and responsive layout.
- Build the full Hugo site; check every catalog/article/related-entry link. Review content samples from all categories and all numerical articles.
- Keep existing local preview running for review, and do not alter existing user changes in the theme or generated public directory.

## Completed — 2026-10-10

- Created all 184 original articles and connected every catalog URL; synchronized topic references into catalog sources.
- Added a responsive article template with desktop/mobile contents, category navigation, adjacent articles and return-to-entry links.
- Updated collection wording and maintenance instructions; added a standard-library integrity checker.
- Full Hugo Extended 0.108.0 build passed (260 total site pages). Validator passed for all 184 articles and 185 knowledge HTML pages: exact eight sections, required metadata, references, related destinations, unique IDs and valid anchors.
- All 184 article URLs returned HTTP 200 from the local server. Desktop 1440px and mobile 390px review passed; checked contents navigation, alias search → article, adjacent article and return-to-directory flows, with no browser warnings/errors observed.
- Reviewed numerical examples and content samples across all categories. Corrected causal interpretation, rebalancing totals, liquidity accounting scope and the constraint-theory capacity example. Sources include DOI/book records where full text may require access.
- Preview remains at http://localhost:1313/knowledge/. No external deployment or Git commit performed; existing theme/public user changes retained.
