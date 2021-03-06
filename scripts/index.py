#!/usr/bin/env python3
# Build Site Index

from glob import iglob
from html import escape
from os.path import dirname
from collections import defaultdict
from re import DOTALL, compile
from yaml import FullLoader, load

# index
tbody = []
groups = defaultdict(list)

# html indent
width = 2
offset = 8
spacer = ' '

# default eol
newline = '\n'

# index excludes
excludes = ('/catalogue.html', '/index.html', '/404.html')

# front matter RegEx
reFrontMatter = compile(r'---\n(.*)\n---', DOTALL)

# path sanitisation RegEx
rePath = compile(r'^src/')

# group index entries
for file in sorted(iglob('src/**', recursive=True)):

  if file.startswith('src/_'):
    continue

  if file.endswith(excludes):
    continue

  if not file.endswith('.html'):
    continue

  with open(file) as document:
    frontmatter = reFrontMatter.match(document.read(-1))

  if not frontmatter:
    continue

  print(f'Indexing file {file}')

  fpath = rePath.sub('', file)
  group = dirname(fpath) or 'generic'
  frontmatter = load(stream=frontmatter.group(1), Loader=FullLoader)

  groups[group].append(newline.join([
    f'{spacer * offset}<tr>',
    f'{spacer * offset}{spacer * width}<td headers="{group}"><a href="{fpath.replace(".html", "")}">{escape(frontmatter["title"])}</a></td>',
    f'{spacer * offset}{spacer * width}<td headers="{group}">{escape(frontmatter.get("desc", "<em>No description available<em>"))}</td>',
    f'{spacer * offset}</tr>'
  ]))

# build index
for group in sorted(groups.keys()):

  tbody.append(newline.join([
    f'{spacer * offset}<tr>',
    f'{spacer * offset}{spacer * width}<th id="{group}" colspan="2">{group.replace("-", " ").title()}</th>',
    f'{spacer * offset}</tr>',
  ]))

  tbody.append(newline.join(groups[group]))

# write index doc
with open(file='src/catalogue.html', mode='wt', encoding='utf_8', newline=newline) as document:
  document.write(newline.join([

    '---',
    'lang: en',
    'title: Catalogue',
    'keywords: ashen, gunaratne, ashen m. gunaratne, educational, tools, materials, catalogue',
    '---',

    '',

    '{%- capture metadata -%}',
    '  <meta charset="UTF-8" />',
    '  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />',
    '  <meta name="description" content="{{ page.desc | default: site.desc }}" />',
    '  <meta name="keywords" content="{{ page.keywords | default: site.keywords }}" />',
    '  <meta name="author" content="{{ site.author | default: site.author }}" />',
    '',
    '  <title>{{ page.title }}</title>',
    '',
    '  <style type="text/css">',
    '',
    '    body {',
    '      margin: 15px;',
    '      font-family: "Segoe UI", "Roboto", "sans-serif";',
    '    }',
    '',
    '    a {',
    '      color: #007bff;',
    '      text-decoration: none;',
    '    }',
    '',
    '    table {',
    '      width: 100%;',
    '      border-collapse: collapse;',
    '      margin-right: auto;',
    '      margin-left: auto;',
    '    }',
    '',
    '    table th,',
    '    table td {',
    '      padding: 0.75rem;',
    '      border-top: 1px solid #e9ecef;',
    '      text-align: left;',
    '    }',
    '',
    '    thead th {',
    '      border-bottom: 2px solid #e9ecef;',
    '    }',
    '',
    '    tbody th {',
    '      color: #6C757D;',
    '      border-top: none;',
    '    }',
    '',
    '    tbody tr:hover {',
    '      background-color: #efefef;',
    '    }',
    '',
    '    tbody tr td:first-child {',
    '      white-space: nowrap;',
    '    }',
    '',
    '    caption {',
    '      color: #868e96;',
    '      padding-top: 0.75rem;',
    '      padding-bottom: 0.75rem;',
    '      caption-side: bottom;',
    '      text-align: center;',
    '    }',
    '',
    '    @media (min-width: 576px) {',
    '      table { max-width: 75vw; }',
    '    }',
    '',
    '    @media (min-width: 768px) {',
    '      table { max-width: 65vw; }',
    '    }',
    '',
    '    @media (min-width: 992px) {',
    '      table { max-width: 55vw; }',
    '    }',
    '',
    '    @media (min-width: 1200px) {',
    '      table { max-width: 45vw; }',
    '    }',
    '',
    '  </style>',
    '{%- endcapture -%}',

    '',

    '{%- capture body -%}',
    '  <main>',
    '    <table>',
    '      <caption>List of Tools</caption>',
    '      <thead>',
    '        <tr>',
    '          <th scope="col">Tool</th>',
    '          <th scope="col">Description</th>',
    '        </tr>',
    '      </thead>',
    '      <tbody>',

             newline.join(tbody),

    '      </tbody>',
    '    </table>',
    '  </main>',
    '{%- endcapture -%}',

    '',

    '{%- include base.html -%}'

  ]))
