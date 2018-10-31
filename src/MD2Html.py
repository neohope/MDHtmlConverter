#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import re
import sys
import codecs
import markdown


css = '''
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<style type="text/css">
<!-- put your css code here -->
</style>
'''

def md2htmlFolder(in_path):
    flist = os.listdir(os.getcwd())
    for in_file in flist:
        if in_file.endswith('.md'):
            out_file=re.sub('md', 'html', in_file)
            md2html(in_file, out_file)


def md2html(in_file, out_file):
    with codecs.open(in_file, mode="r", encoding="utf-8") as fr:
        text = fr.read()
    html = markdown.markdown(text)
    with codecs.open(out_file, "w",encoding="utf-8",errors="xmlcharrefreplace") as fo:
        fo.write(css+html)


if __name__ == "__main__":
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    md2html(in_file, out_file)

