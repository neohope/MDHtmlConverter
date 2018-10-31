#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import re
import sys
import html2text


def html2mdFolder(in_path):
    flist = os.listdir(os.getcwd())
    for in_file in flist:
        if in_file.endswith('.html'):
            out_file=re.sub('html', 'md', in_file)
            html2md(in_file, out_file)


def html2md(in_file, out_file):
    with open(in_file, 'r', encoding='utf8') as f:
        md = html2text.html2text(f.read())
        pattern = r'-\n'
        md_text = re.sub(pattern, '-', md)
        with open(out_file, 'w', encoding='utf8') as nf:
            nf.write(md_text)


if __name__ == "__main__":
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    html2md(in_file, out_file)

