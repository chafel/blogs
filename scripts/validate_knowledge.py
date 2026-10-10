#!/usr/bin/env python3
"""Check article coverage, structure, references and generated knowledge links.

Usage: python3 scripts/validate_knowledge.py [--build-dir /path/to/hugo/output]
Uses only the Python standard library. Knowledge articles use JSON front matter
inside YAML fences (JSON is valid YAML), so no YAML dependency is needed.
"""
import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
HEADINGS = ['一个具体问题', '一句话解释', '出处与原意', '原理与机制',
            '一个完整案例', '适用条件与反例', '今天可以尝试的行动', '参考资料与关联条目']


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids, self.links = [], []
        self.unrendered_emphasis = []
        self.code_depth = 0
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        if tag in ('code', 'pre'):
            self.code_depth += 1
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])

    def handle_endtag(self, tag):
        if tag in ('code', 'pre'):
            self.code_depth = max(0, self.code_depth - 1)

    def handle_data(self, data):
        if not self.code_depth:
            self.unrendered_emphasis.extend(re.findall(r'\*\*[^*\n]+\*\*', data))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build-dir', type=Path)
    args = parser.parse_args()
    catalog = json.loads((ROOT / 'data/knowledge.json').read_text())
    entries = [i for c in catalog['categories'] for i in c['items']]
    ids = {i['id'] for i in entries}
    errors, lengths = [], []
    if len(ids) != len(entries):
        errors.append('Duplicate catalog entry IDs')
    paths = {p.stem: p for p in (ROOT / 'content/knowledge').glob('*.md') if p.stem != '_index'}
    for extra in paths.keys() - ids:
        errors.append(f'Article missing from catalog: {extra}')
    for item in entries:
        key = item['id']
        if key not in paths:
            errors.append(f'Missing article: {key}')
            continue
        if item['url'] != f'/knowledge/{key}/':
            errors.append(f'{key}: catalog URL does not match article')
        try:
            _, raw_meta, body = paths[key].read_text().split('---', 2)
            meta = json.loads(raw_meta)
        except (ValueError, json.JSONDecodeError):
            errors.append(f'{key}: invalid JSON front matter')
            continue
        for field, expected in [('knowledge_id', key), ('title', item['name']),
                                ('type', 'knowledge'), ('draft', False)]:
            if meta.get(field) != expected:
                errors.append(f'{key}: invalid {field}')
        headings = re.findall(r'^## (.+)$', body, re.M)
        if headings != [f'{n}. {h}' for n, h in enumerate(HEADINGS, 1)]:
            errors.append(f'{key}: expected the eight standard sections')
        refs = body.split('## 8. 参考资料与关联条目')[-1]
        external = re.findall(r'\]\((https?://[^\s)]+)\)', refs)
        if not external:
            errors.append(f'{key}: missing source links')
        if not re.search(r'假设|虚构|示例', body.split('## 5.')[-1].split('## 6.')[0]):
            errors.append(f'{key}: example needs an explicit hypothetical label')
        related = re.findall(r'\]\(/knowledge/([^/#]+)/\)', refs)
        if len(set(related)) < 2:
            errors.append(f'{key}: fewer than two related articles')
        for target in re.findall(r'\]\(/knowledge/([^/#]+)/\)', body):
            if target not in ids:
                errors.append(f'{key}: unknown related article {target}')
        lengths.append(len(re.findall(r'[\u4e00-\u9fff]', body)))
    if args.build_dir:
        directory = args.build_dir.resolve()
        pages = {}
        for route in ['/knowledge/'] + [f'/knowledge/{key}/' for key in sorted(ids)]:
            path = directory / route.lstrip('/') / 'index.html'
            if not path.is_file():
                errors.append(f'Missing rendered page: {route}')
                continue
            pages[route] = Page(path)
        for route, page in pages.items():
            if page.unrendered_emphasis:
                errors.append(f'{route}: unrendered Markdown emphasis {page.unrendered_emphasis}')
            duplicates = [key for key, count in Counter(page.ids).items() if count > 1]
            if duplicates:
                errors.append(f'{route}: duplicate HTML IDs {duplicates}')
            for link in page.links:
                target = urlsplit(link)
                if target.scheme or target.netloc:
                    continue
                target_route = target.path or route
                if not target_route.startswith('/knowledge/'):
                    continue
                if target_route not in pages:
                    errors.append(f'{route}: broken local link {link}')
                elif target.fragment and unquote(target.fragment) not in pages[target_route].ids:
                    errors.append(f'{route}: missing anchor {link}')
    if errors:
        print('\n'.join(errors))
        raise SystemExit(1)
    print(f'PASS: {len(entries)} articles across {len(catalog["categories"])} categories; '
          'front matter, eight sections, sources and related links valid.')
    print(f'Chinese characters (including headings/references): {sum(lengths):,}; '
          f'range per article: {min(lengths)}–{max(lengths)}.')
    if args.build_dir:
        print(f'PASS: {len(pages)} rendered pages; no duplicate IDs, broken knowledge links or anchors.')


if __name__ == '__main__':
    main()
