#!/usr/bin/env python3.6

from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import select_autoescape
import os.path


HOME_URL='https://jakub-m.github.io/szacowanie.elblag.pl'


def main():
    env = Environment(
        loader=FileSystemLoader('templates/'),
        autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('main.tpl')

    pages = [
        {
            'file_name': 'index.html',
            'name':'Strona główna'
        }, {
            'file_name': 'ceny-uslug.html',
            'name':'Ceny usług'
        }, {
            'file_name': 'wymagane-dokumenty.html',
            'name':'Wymagane dokumenty'
        }, {
            'file_name': 'uprawnienia.html',
            'name':'Uprawnienia'
        }, {
            'file_name': 'linki.html',
            'name':'Linki'
        },
    ]
    for page in pages:
        output_path = os.path.join('docs', page['file_name'])
        sidebar_items = [{
                            'abs_path': HOME_URL + '/' + p['file_name'],
                            'a_class': 'current' if p['file_name'] == page['file_name'] else '',
                            'a_name': p['name']
                           } for p in pages]
        with open(output_path, 'w') as h:
            h.write(template.render(content_path='/' + page['file_name'],
                                    home_url=HOME_URL,
                                    sidebar_items=sidebar_items))

main()

