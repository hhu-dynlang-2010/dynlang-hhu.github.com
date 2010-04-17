import os
import os.path

class Builder(object):
    inext = None # abstract base class
    outext = None

    def __init__(self, path, input):
        self.path = path
        self._input = input
        purebasename, suffix = input.rsplit(".", 1)
        self.suffix = suffix
        self.purebasename = purebasename
        self._output = purebasename + self.outext
        with open(self.input()) as f:
            s = f.read()
        self.content = s

    def applicable(self):
        return True

    def input(self):
        return os.path.join(self.path, self._input)
    def output(self):
        return os.path.join(self.path, self._output)
    def join(self, filename):
        return os.path.join(self.path, filename)

    def recent_output(self):
        try:
            return (os.stat(self.input()).st_mtime <
                    os.stat(self.output()).st_mtime)
        except OSError:
            return False

    def build(self):
        if self.recent_output():
            return
        print "building", self.output(), "with", self.__class__.__name__
        if not self._build() or not self.recent_output():
            print "building of %s failed" % (self.output(), )

class BeamerBuilder(Builder):
    inext = "rst"
    outext = ".pdf"

    def applicable(self):
        return '<s5defs.txt>' in self.content

    def _build(self):
        latexfile = self.join(self.purebasename + ".latex")
        cmd = './rst2beamer.py %s > %s' % (self.input(), latexfile)
        if os.system(cmd):
            return False
        # amazing, isn't it?
        replace(latexfile, '\\author{}', '\\author{Carl Friedrich Bolz, David Schneider\nDynamische Programmiersprachen\nHeinrich-Heine-Universit\\"at D\\"usseldorf\nSommersemester 2010}'.replace('\n', '\\\\\n'))
        for i in range(2):
            cmd = "pdflatex " + latexfile
            if os.system(cmd):
                return False
        for suffix in "aux log nav out toc snm".split():
            os.remove(self.join(self.purebasename  + "." + suffix))
        return True

class RstHtmlBuilder(Builder):
    inext = "rst"
    outext = ".html"

    def applicable(self):
        return '<s5defs.txt>' not in self.content

    def _build(self):
        cmd = 'rst2html.py --input-encoding=utf8 --output-encoding=utf8 --stylesheet-path=style.css %s %s' % (self.input(), self.output())
        if os.system(cmd):
            return False
        if self._input == "index.txt":
            replace(self.output(),
        """http://docutils.sourceforge.net/" />
<title>""",
        """http://docutils.sourceforge.net/" />
<link rel="alternate" type="application/rss+xml" title="RSS-Feed" href="lecture-rss.xml" />
<title>""")
        return True

class PygmentizeBuilder(Builder):
    outext = ".html"

    def _build(self):
        cmd = 'pygmentize -l %s -o %s -O full,linenos,style=manni,cssfile=highlight.css %s' % (self.syntax, self.output(), self.input())
        if os.system(cmd):
            return False
        return True

class PyBuilder(PygmentizeBuilder):
    inext = "py"
    syntax = "py"

    def applicable(self):
        return self.purebasename not in ["rebuild", "rst2beamer", "rss"]

class PyConsoleBuilder(PygmentizeBuilder):
    inext = "pyi"
    syntax = "pycon"

class DotBuilder(Builder):
    inext = "dot"
    outext = ".pdf"

    def _build(self):
        epsname = self.join(self.purebasename + ".eps")
        cmd = 'dot -Teps %s -o %s && epstopdf %s' % (self.input(), epsname, epsname)
        if os.system(cmd):
            return False
        return True

builders = {}
for cls in [BeamerBuilder, RstHtmlBuilder, PyBuilder, PyConsoleBuilder, DotBuilder]:
    builders.setdefault(cls.inext, []).append(cls)

def process(l):
    for dir, basename in l:
        if "." not in basename:
            continue
        purebasename, suffix = basename.rsplit(".", 1)
        fullpath = os.path.join(dir, basename)
        if suffix not in builders:
            continue
        for B in builders[suffix]:
            b = B(dir, basename)
            if not b.applicable():
                continue
            b.build()
            break

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
