# -*- coding: utf-8 -*-
from glob import glob
from os import path, makedirs
from codecs import open
from shutil import copytree, rmtree

import markdown
from jinja2 import Template

MENU = [
    {'file': 'index', 'icon': 'icon-info-sign', 'name': u'책 소개'},
    {'file': 'peek', 'icon': 'icon-book', 'name': u'미리 보기'},
    {'file': 'problems', 'icon': 'icon-question-sign', 'name': u'연습 문제'},
    {'file': 'errata', 'icon': 'icon-ok', 'name': u'정오표'},
    {'file': 'buy', 'icon': 'icon-shopping-cart', 'name': u'구입하기'},
]

template = Template(open('template.html', encoding='utf-8').read())
# md = markdown.Markdown()

def compile_page(source, dest):
    s = open(source, encoding='utf-8') 
    d = open(dest, 'w', encoding='utf-8')
    compiled = markdown.markdown(s.read(), ['footnotes', 'tables'])
    d.write(template.render(MENU=MENU, content=compiled))
    print 'generated', dest

def main():

    if path.exists('output'): 
        rmtree('output')
    makedirs('output')

    for source in glob('pages/*.md'): 
        page_name = '.'.join(path.basename(source).split('.')[:-1])
        dest = path.join('output', page_name + '.html')
        compile_page(source, dest)

    copytree('static', 'output/static')

if __name__ == '__main__':
    main()
