#!/usr/bin/env python
import re
import markdown
import subprocess


class MyPreprocessor(markdown.preprocessors.Preprocessor):
    BLOCK_RE = re.compile(r'''
        ::shellcmd::\s*([^\n]*)
        '''
        , re.VERBOSE)
    BLOCK_RE2 = re.compile(r'''
        ::shellcmd-start::\s*\n(.*?)\n\s*
        ::shellcmd-end::[ ]*$
        ''', re.MULTILINE | re.DOTALL | re.VERBOSE)

    def __init__(self, md):
        super(MyPreprocessor, self).__init__(md)

    def run(self, lines):
        text = '\n'.join(lines)
        did_replace = True

        while did_replace:
            text, did_replace = self._replace_block(text)

        return text.split('\n')

    def _replace_block(self, text):
        # Parse configuration params
        m = MyPreprocessor.BLOCK_RE.search(text)
        if not m:
            m = MyPreprocessor.BLOCK_RE2.search(text)
            if not m:
                return text, False
            else:
                cmds = m.group(1).rstrip('\r\n').split('\n')
        else:
            cmds = [m.group(1)]
        output=""
        for cmd in cmds:
            p=subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True)
            res, _ = p.communicate()
            res = res.decode("utf-8").rstrip('\r\n')
            res = "\t"+res.replace("\n", "\n\t")+"\n"
            output += res;
        return text[:m.start()] + output + text[m.end():], True


# For details see https://pythonhosted.org/Markdown/extensions/api.html#extendmarkdown
class MyMarkdownExtension(markdown.Extension):
    # For details see https://pythonhosted.org/Markdown/extensions/api.html#configsettings
    def __init__(self, *args, **kwargs):
        self.config = {
        }

        super(MyMarkdownExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        blockprocessor = MyPreprocessor(md)
        blockprocessor.config = self.getConfigs()
        # need to go before both fenced_code_block and things like retext's PosMapMarkPreprocessor
        md.preprocessors.add('shellcmd', blockprocessor, '_begin')


def makeExtension(*args, **kwargs):
    return MyMarkdownExtension(*args, **kwargs)
