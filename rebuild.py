import os
import os.path

def make_pdf(basename, suffix):
    cmd = './rst2beamer.py %s.%s > %s.latex' % (basename, suffix, basename)
    if os.system(cmd):
        raise Exception
    # amazing, isn't it?
    replace('%s.latex' % (basename, ), 'author{}', 'author{Carl Friedrich Bolz, David Schneider\nDynamische Programmiersprachen\nHeinrich-Heine-Universit\\"at D\\"usseldorf\nSommersemester 2010}'.replace('\n', '\\\\\n'))
    cmd = "pdflatex %s.latex" % (basename, )
    if os.system(cmd):
        raise Exception
    cmd = "pdflatex %s.latex" % (basename, )
    if os.system(cmd):
        raise Exception
    for suffix in "aux log nav out toc snm".split():
        os.remove("%s.%s" % (basename, suffix))

def recent_output(dir, input, output):
    try:
        return (os.stat(os.path.join(dir, input)).st_mtime <
                os.stat(os.path.join(dir, output)).st_mtime)
    except OSError:
        return False


def process(l):
    for dir, basename in l:
        if "." not in basename:
            continue
        purebasename, suffix = basename.rsplit(".", 1)
        fullpath = os.path.join(dir, basename)
        if suffix == 'txt' or suffix == 'rst':
            output = purebasename + ".html"
            fullpath = os.path.join(dir, basename)
            f = open(fullpath, 'r')
            data = f.read()
            f.close()
            if '<s5defs.txt>' in data:
                output = purebasename + ".pdf"
                if recent_output(dir, basename, output):
                    print "building of %s not necessary" % (output, )
                    continue
                make_pdf(purebasename, suffix)
                continue
            else:
                output = purebasename + ".html"
                if recent_output(dir, basename, output):
                    print "building of %s not necessary" % (output, )
                    continue
                cmd = 'rst2html.py --input-encoding=utf8 --output-encoding=utf8 --stylesheet-path=style.css %s.txt %s' % (purebasename, output)
        elif suffix == 'py' and purebasename not in ["rebuild", "rst2beamer"]:
            output = basename + ".html"
            if recent_output(dir, basename, output):
                print "building of %s not necessary" % (output, )
                continue
            cmd = 'pygmentize -l %s -o %s -O full,linenos,style=manni,cssfile=highlight.css %s' % (suffix, output, fullpath)
        elif suffix == 'pyi':
            output = purebasename + ".html"
            if recent_output(dir, basename, output):
                print "building of %s not necessary" % (output, )
                continue
            cmd = 'pygmentize -l pycon -o %s -O full,linenos,style=manni,cssfile=highlight.css %s' % (output, fullpath)
        elif suffix == "dot":
            output = purebasename + ".pdf"
            print output
            if recent_output(dir, basename, output):
                print "building of %s not necessary" % (output, )
                continue
            epsname = os.path.join(dir, purebasename + ".eps")
            cmd = 'dot -Teps %s -o %s && epstopdf %s' % (fullpath, epsname, epsname)

        else:
            continue
        print '*', cmd
        os.system(cmd)
        if output == "index.html":
            replace(output,
        """http://docutils.sourceforge.net/" />
<title>""",
        """http://docutils.sourceforge.net/" />
<link rel="alternate" type="application/rss+xml" title="RSS-Feed" href="lecture-rss.xml" />
<title>""")

def replace(filename, search, replace):
    with file(filename) as f:
        s = f.read()
    s = s.replace(search, replace)
    with file(filename, "w") as f:
        f.write(s)

def main():
    import sys
    if len(sys.argv) == 1:
        files = [(dir, fn) for dir in ['.', 'aufgaben', 'figures'] for fn in os.listdir(dir)]
        process(files)
    else:
        process([(os.path.dirname(arg), os.path.basename(arg)) for arg in sys.argv[1:]])


if __name__ == '__main__':
    main()
