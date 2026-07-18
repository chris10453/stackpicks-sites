# Canonical StackPicks Site Template Rules

Every new affiliate site and page starts from `template/`. Do not copy a prior live site as the starting point.

## Non-negotiable portfolio rules

- Keep the disclosure block above the first commercial CTA/offer link in document order. The first CTA must not appear in navigation, hero, cards, or body copy before the disclosure.
- Email forms are banned portfolio-wide until a real backend exists. Do not add `<form>` elements, `action="#"`, newsletter capture, or fake POST handlers.
- Do not use star ratings, five-point product ratings, emoji-star scores, or review-platform ratings.
- Do not publish unsourced statistics. Every number that materially supports a product or outcome claim needs a traceable source in the page or it is removed.
- Do not promise outcomes or use guarantee language. Qualify product claims (`may`, `can be a fit`, `individual results vary`). Vendor refund terms may be described as vendor-stated terms, never as a promise of results.
- Scores must be rubric-labeled shopping-information scores only (for example, `Checkout-Clarity Score`). Never imply efficacy, safety, financial performance, or suitability.
- Every page includes the publisher identity block with brand, research-team attribution, and `mailto:stackpicksmedia@gmail.com`.
- Every site includes `privacy.html`, `terms.html`, `affiliate-disclosure.html`, and a working `sitemap.xml`.
- Sitemap URLs must use the real configured site domain. Generate with `scripts/generate-sitemap.py --base-url https://example.invalid/site` and replace the example only at build time.
- Products marked `insufficient info to rate` remain information-only rows: suppress the BUY/offer link and give a one-line reason naming the unverifiable fact.
- If a redirect uses a different official checkout domain, state that on-page so the redirect is expected and not scam-flavored.

## Boilerplate blocks

The following blocks are canonical and may not be removed or weakened. Customize only the marked site/page values:

- `boilerplate/disclosure.html` — disclosure placement and wording
- `boilerplate/identity.html` — publisher identity/contact
- `boilerplate/legal-links.html` — legal-page links
- `boilerplate/score-label.html` — rubric-labeled score limitation

The HTML comments in `index.html` are guardrails for generators and reviewers. A build that drops a block fails review.

## Release checklist

- [ ] Started from `template/`.
- [ ] Disclosure block appears before the first commercial CTA.
- [ ] No `<form>` or `action="#"` anywhere in the live tree.
- [ ] No stars or star-based ratings.
- [ ] No unsourced statistics.
- [ ] No outcome guarantees or unqualified guarantee language.
- [ ] Scores are labeled with the shopping-information rubric.
- [ ] Identity block and contact email are present.
- [ ] Privacy, terms, and affiliate-disclosure pages exist.
- [ ] Sitemap generator ran with the real domain; sitemap parses and contains no placeholders/internal URLs.
- [ ] `insufficient info to rate` rows have no BUY/offer link and include a one-line reason.
- [ ] Vendor-domain mismatch notes are present where a redirect domain differs.
- [ ] Run `/home/ai/AI-Operating-System/scripts/verify-affiliate-sites.sh` and paste the complete output in the handoff.
