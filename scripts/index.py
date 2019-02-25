#!/usr/bin/env python3
# Build Site Index

from yaml import load
from glob import iglob
from re import DOTALL, compile

# index
tbody = []

# html indent
width = 2
offset = 14
spacer = ' '

# default eol
newline = '\n'

# index excludes
excludes = ('index.html', 'legend.html', '404.html')

# front matter RegEx
reFrontMatter = compile(r'---\n(.*)\n---', DOTALL)

# build index
for file in sorted(iglob('**', recursive=True)):

  if file.startswith('_'):
    continue

  if file.endswith(excludes):
    continue

  if not file.endswith('.html'):
    continue

  with open(file) as document:
    frontmatter = reFrontMatter.match(document.read(-1))

  if not frontmatter:
    continue

  frontmatter = load(frontmatter.group(1))

  tbody.append(newline.join([
    f'{spacer * offset}<tr>',
    f'{spacer * offset}{spacer * width}<td><a href="{file.replace(".html", "")}">{frontmatter["title"]}</a></td>',
    f'{spacer * offset}{spacer * width}<td>{frontmatter.get("desc", "<em>No description available<em>")}</td>',
    f'{spacer * offset}</tr>'
  ]))

# write index doc
with open(file='legend.html', mode='wt', encoding='utf_8', newline=newline) as document:
  document.write(newline.join([

    '---',
    'lang: en',
    'title: Index',
    'keywords: ashen, gunaratne, ashen m. gunaratne, educational, tools, materials, index',
    '---',

    '',

    '{%- capture metadata -%}',
    '  <meta charset="UTF-8" />',
    '  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />',
    '  <meta name="description" content="{{ page.desc }}" />',
    '  <meta name="keywords" content="{{ page.keywords }}" />',
    '  <meta name="author" content="{{ site.author }}" />',
    '',
    '  <title>{{ page.title }}</title>',
    '',
    '  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous" />',
    '',
    '  <style type="text/css">',
    '',
    '    table {',
    '      margin: 20px;',
    '    }',
    '',
    '    caption {',
    '      text-align: center;',
    '    }',
    '',
    '  </style>',
    '{%- endcapture -%}',

    '',

    '{%- capture body -%}',
    '  <main>',
    '    <div class="container-fluid">',
    '      <div class="row justify-content-center">',
    '        <div class="col-md-6">',
    '          <table class="table table-hover table-responsive-sm">',
    '            <caption>List of Tools</caption>',
    '            <thead>',
    '              <tr>',
    '                <th scope="col">Tool</th>',
    '                <th scope="col">Description</th>',
    '              </tr>',
    '            </thead>',
    '            <tbody>',

                   newline.join(tbody),

    '            </tbody>',
    '          </table>',
    '        </div>',
    '      </div>',
    '    </div>',
    '  </main>',
    '{%- endcapture -%}',

    '',

    '{%- include base.html -%}'

  ]))
