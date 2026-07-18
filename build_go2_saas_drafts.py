from pathlib import Path
from html import escape
from datetime import datetime, timezone

ROOT = Path('/home/ai/stackpicks-sites/factory-drafts')
CHECKED = '2026-07-18'
PAGES = {
    'saas-project-management': {
        'title': 'Project management software: Asana vs ClickUp vs Trello',
        'lede': 'A decision-first comparison for teams choosing a project workspace. We focus on structure, permissions, exports, integrations, and plan boundaries—not feature-count theater.',
        'vendors': [
            ('Asana', 'Best fit to investigate when work needs clear project structure, owners, timelines, and repeatable workflows.', 'https://asana.com/pricing', 'Check current seat rules, plan limits, admin controls, and export options before purchase.'),
            ('ClickUp', 'Best fit to investigate when a team wants a highly configurable workspace and is willing to manage more setup complexity.', 'https://clickup.com/pricing', 'Check current feature availability by plan, guest/member rules, and whether the configuration is maintainable for the team.'),
            ('Trello', 'Best fit to investigate when a lightweight board workflow is more valuable than a broad operations suite.', 'https://trello.com/pricing', 'Check board, automation, attachment, admin, and export limits at the team size you expect.'),
        ],
        'checks': ['Team shape and workflow', 'Permissions and guest access', 'Exports and portability', 'Integrations and automation', 'Billing and plan boundaries'],
        'questions': ['Can a new teammate understand the workflow without a training session?', 'What happens when a guest, contractor, or external client needs access?', 'Can you export the work in a usable format if the vendor changes terms?', 'Which automation rules are essential rather than nice-to-have?', 'What limit will you hit first: seats, projects, storage, automations, or permissions?'],
    },
    'saas-email-marketing': {
        'title': 'Email marketing software: MailerLite vs Brevo vs Mailchimp',
        'lede': 'A practical shortlist for small teams comparing email tools. We compare list definitions, automation depth, sending model, templates, exports, and billing language.',
        'vendors': [
            ('MailerLite', 'Best fit to investigate when a small team wants a focused campaign and automation workflow with a simple starting surface.', 'https://www.mailerlite.com/pricing', 'Check current subscriber bands, sending limits, automation features, and what is included in the plan you would actually use.'),
            ('Brevo', 'Best fit to investigate when sending volume and contact storage need to be considered separately.', 'https://www.brevo.com/pricing/', 'Check current daily/monthly send rules, automation limits, transactional-email separation, and overage language.'),
            ('Mailchimp', 'Best fit to investigate when a team values a mature ecosystem and accepts the need to study audience, seat, and feature boundaries carefully.', 'https://mailchimp.com/pricing/', 'Check current audience-counting rules, seats, automation, templates, and archive/export behavior.'),
        ],
        'checks': ['Subscriber and audience definition', 'Sending model and overages', 'Automation depth', 'Templates and landing pages', 'Export, consent, and unsubscribe controls'],
        'questions': ['Does the vendor count subscribed, archived, and unsubscribed contacts separately?', 'Is billing driven by contacts, sends, seats, or a mix?', 'Can you export contacts and campaign data without a support ticket?', 'Which automation trigger and branching rules are available on the intended plan?', 'Can the team demonstrate consent, unsubscribe, and suppression handling?'],
    },
    'saas-crm': {
        'title': 'CRM software: HubSpot vs Zoho CRM vs Pipedrive',
        'lede': 'A research-led CRM comparison for small teams. We separate contact storage from pipeline workflow, reporting, automation, integrations, and migration risk.',
        'vendors': [
            ('HubSpot CRM', 'Best fit to investigate when a team wants a broad ecosystem and needs to map which capabilities belong to which hub or tier.', 'https://www.hubspot.com/pricing/crm', 'Check current seat, hub, marketing, reporting, automation, and data-retention boundaries.'),
            ('Zoho CRM', 'Best fit to investigate when a team wants a configurable CRM inside a larger business-software ecosystem.', 'https://www.zoho.com/crm/zohocrm-pricing.html', 'Check current edition limits, automation, customization, storage, support, and integration terms.'),
            ('Pipedrive', 'Best fit to investigate when a sales pipeline is the center of the workflow and a focused interface is preferred.', 'https://www.pipedrive.com/en/pricing', 'Verify current pricing and feature details directly in the vendor flow; automated access returned HTTP 403 during this pass.'),
        ],
        'checks': ['Pipeline fit and required stages', 'Contact/company data model', 'Automation and reporting', 'Integrations and permissions', 'Export and migration path'],
        'questions': ['Can the team model its real sales stages without spreadsheet sidecars?', 'What fields, activities, and relationships must be preserved during import?', 'Which reports are available without an upgrade or custom work?', 'How are roles, teams, and visibility rules handled?', 'Can the full dataset and activity history be exported in a usable format?'],
    },
}

CSS = '''*{box-sizing:border-box}body{margin:0;background:#f7fffe;color:#082f49;font:16px/1.65 system-ui,-apple-system,sans-serif}a{color:#0f766e}.wrap{max-width:1060px;margin:auto;padding:0 20px 64px}.draft{background:#0f766e;color:#fff;padding:10px 14px;text-align:center;font-size:.9rem}.eyebrow{color:#0f766e;font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:.78rem}h1{font-size:clamp(2rem,5vw,4rem);line-height:1.05;max-width:850px;margin:14px 0}.lede{font-size:1.18rem;max-width:800px;color:#395466}.notice,.gate,.card,table,details{background:#fff;border:1px solid #c7ddda;border-radius:14px}.notice,.gate{padding:18px;margin:22px 0}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin:20px 0}.card{padding:20px}.card h2{margin-top:0}.label{font-size:.8rem;text-transform:uppercase;letter-spacing:.06em;color:#526477;font-weight:700}table{width:100%;border-collapse:separate;border-spacing:0;overflow:hidden;margin:20px 0}th,td{text-align:left;vertical-align:top;padding:14px;border-bottom:1px solid #dbe9e6}th{background:#e7f6f2}tr:last-child td{border-bottom:0}details{padding:14px 16px;margin:10px 0}summary{font-weight:700;cursor:pointer}footer{border-top:1px solid #c7ddda;padding-top:18px;color:#526477;font-size:.9rem;margin-top:34px}nav{display:flex;gap:18px;flex-wrap:wrap;padding:22px 0;border-bottom:1px solid #c7ddda}'''

def legal(slug, title):
    base = ROOT / slug
    for name, heading, text in [
        ('affiliate-disclosure.html','Affiliate Disclosure','We may earn a commission from a marked link after approval. Commercial relationships do not determine the comparison criteria. Product facts and program terms must be rechecked before publication.'),
        ('privacy.html','Privacy Policy','This staging draft does not collect form submissions or create accounts. If the page is published with analytics or email capture, this policy must be updated before launch.'),
        ('terms.html','Terms of Use','This is decision-support content, not legal, financial, medical, or professional advice. Vendor terms, prices, features, and availability can change; check the linked source before acting.'),
    ]:
        (base/name).write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{heading} | StackPicks</title><style>{CSS}</style></head><body><div class="wrap"><nav><a href="index.html">Back to {escape(title)}</a></nav><main><p class="eyebrow">StackPicks research desk</p><h1>{heading}</h1><p>{text}</p></main><footer><p>Research and reviews by the StackPicks research team. Contact: <a href="mailto:stackpicksmedia@gmail.com">stackpicksmedia@gmail.com</a></p></footer></div></body></html>\n', encoding='utf-8')

def build(slug, data):
    base = ROOT / slug
    base.mkdir(parents=True, exist_ok=True)
    rows = ''.join(f'<tr><td><strong>{escape(v)}</strong></td><td>{escape(summary)}</td><td><a href="{url}">Official source</a><br><small>{escape(note)}</small></td></tr>' for v, summary, url, note in data['vendors'])
    cards = ''.join(f'<article class="card"><p class="label">Decision lens {i}</p><h2>{escape(x)}</h2><p>Record the exact source, date checked, and boundary before treating this as a comparison fact.</p></article>' for i,x in enumerate(data['checks'],1))
    questions = ''.join(f'<details><summary>{escape(q)}</summary><p>Answer from the vendor documentation and a dated hands-on check. If the answer is unavailable, mark it unknown rather than inferring it.</p></details>' for q in data['questions'])
    html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(data['title'])} | StackPicks</title><meta name="description" content="{escape(data['lede'])}"><meta name="site-id" content="{slug}"><meta name="publish-flag" content="draft"><style>{CSS}</style></head><body><div class="draft">STAGING DRAFT · NOT LIVE · Full source and commercial gates required before publication</div><div class="wrap"><nav><a href="../../index.html">StackPicks</a><a href="affiliate-disclosure.html">Disclosure</a><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a></nav><main><p class="eyebrow">StackPicks research desk · {slug}</p><h1>{escape(data['title'])}</h1><p class="lede">{escape(data['lede'])}</p><div class="notice"><strong>Editorial boundary:</strong> This draft makes no claim of first-hand use, lowest price, best performance, or guaranteed outcome. Vendor facts are linked to official sources and must be rechecked on the publication date.</div><h2>Shortlist with honest fit</h2><table><thead><tr><th>Vendor</th><th>Why it belongs in the shortlist</th><th>Gate source and recheck note</th></tr></thead><tbody>{rows}</tbody></table><h2>What this guide checks</h2><div class="grid">{cards}</div><h2>Questions a buyer should answer</h2>{questions}<div class="gate"><p class="label">Publication gates</p><ol><li>Recheck every official source and record the date.</li><li>Add comparable plan/feature evidence for all three vendors; do not compare one vendor's marketing copy to another's support article.</li><li>Verify commercial program approval and tracking links before displaying any vendor CTA.</li><li>Run link, mobile, accessibility, disclosure, and fresh-eyes review probes.</li><li>Publish only after HTTPS enforcement and the proposed order gate clears.</li></ol><p><strong>Last source-check date:</strong> {CHECKED}. <strong>Current status:</strong> content-ready research draft; not published.</p></div></main><footer><p>Research and reviews by the StackPicks research team. Contact: <a href="mailto:stackpicksmedia@gmail.com">stackpicksmedia@gmail.com</a></p><p><a href="affiliate-disclosure.html">Affiliate Disclosure</a> · <a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a></p></footer></div></body></html>'''
    (base/'index.html').write_text(html, encoding='utf-8')
    legal(slug, data['title'])

for slug, data in PAGES.items():
    build(slug, data)
print(f'BUILT {len(PAGES)} SaaS comparison drafts: {", ".join(PAGES)}')
