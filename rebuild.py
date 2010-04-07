import os

for dir in ['.', 'aufgaben']:
    for fn in os.listdir(dir):
        if "." not in fn:
            continue
        purebasename, suffix = fn.rsplit(".", 1)
        if suffix == 'txt':
            filename = os.path.join(dir, fn)
            f = open(filename, 'r')
            data = f.read()
            f.close()
            basename = filename[:-4]
            if '<s5defs.txt>' in data:
                cmd = 'rst2s5.py %s.txt %s.html' % (basename, basename)
            else:
                cmd = 'rst2html.py --input-encoding=utf8 --output-encoding=utf8 --stylesheet-path=style.css %s.txt %s.html' % (basename, basename)
        elif suffix == 'py' or suffix == 'pycon':
            filename = os.path.join(dir, fn)
            cmd = 'pygmentize -l %s -o %s.html -O full,linenos,style=manni,cssfile=highlight.css %s' % (suffix, filename, filename)
        else:
            continue
        print '*', cmd
        os.system(cmd)
