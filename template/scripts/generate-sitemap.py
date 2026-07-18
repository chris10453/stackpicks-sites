#!/usr/bin/env python3
"""Generate a sitemap from live HTML files using an explicit real base URL."""
from __future__ import annotations
import argparse
from pathlib import Path
from urllib.parse import urljoin
from xml.etree.ElementTree import Element, SubElement, ElementTree

parser = argparse.ArgumentParser()
parser.add_argument('--base-url', required=True, help='Real public site URL, e.g. https://example.com/reviews')
parser.add_argument('--root', default='.', help='Site directory to scan')
parser.add_argument('--output', default='sitemap.xml')
args = parser.parse_args()
base = args.base_url.rstrip('/') + '/'
if any(x in base.lower() for x in ('example.com', 'example.invalid', 'localhost', '127.0.0.1', '100.88.')):
    raise SystemExit('refusing placeholder/internal base URL; pass the real public domain')
root = Path(args.root)
urls = []
for page in sorted(root.rglob('*.html')):
    if any(part in {'drafts', 'template', '.git'} for part in page.parts):
        continue
    rel = page.relative_to(root).as_posix()
    if rel == 'index.html':
        path = ''
    elif rel.endswith('/index.html'):
        path = rel[:-len('index.html')]
    else:
        path = rel
    urls.append(urljoin(base, path))
urlset = Element('urlset', {'xmlns': 'http://www.sitemaps.org/schemas/sitemap/0.9'})
for url in urls:
    item = SubElement(urlset, 'url')
    loc = SubElement(item, 'loc')
    loc.text = url
ElementTree(urlset).write(args.output, encoding='utf-8', xml_declaration=True)
print(f'generated {args.output}: {len(urls)} URLs from {base}')
