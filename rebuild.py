import os

def make_pdf(basename):
    cmd = './rst2beamer.py %s.txt > %s.latex' % (basename, basename)
    if os.system(cmd):
        raise Exception
    # amazing, isn't it?
    cmd = "sed 's/\\\\author{}/\\\\author{Carl Friedrich Bolz, David Schneider\\\\\\\\\\nHeinrich-Heine-Universit\\\\\"at D\\\\\"usseldorf\\\\\\\\\\nSommersemester 2010}/' -i %s.latex" % (basename, )
    print cmd
    if os.system(cmd):
        raise Exception
    cmd = "pdflatex %s.latex" % (basename, )
    if os.system(cmd):
        raise Exception
    cmd = "pdflatex %s.latex" % (basename, )
    if os.system(cmd):
        raise Exception
    for suffix in "aux log nav out toc snm".split():
        os.remove("%s.%s" % (basename, suffix))



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
                make_pdf(basename)
                continue
            else:
                cmd = 'rst2html.py --input-encoding=utf8 --output-encoding=utf8 --stylesheet-path=style.css %s.txt %s.html' % (basename, basename)
        elif suffix == 'py' and purebasename not in ["rebuild", "rst2beamer"]:
            filename = os.path.join(dir, fn)
            cmd = 'pygmentize -l %s -o %s.html -O full,linenos,style=manni,cssfile=highlight.css %s' % (suffix, filename, filename)
        else:
            continue
        print '*', cmd
        os.system(cmd)
