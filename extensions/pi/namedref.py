#!/usr/bin/env python
import re
import markdown
import subprocess


class MyPreprocessor(markdown.preprocessors.Preprocessor):
    BLOCK_RE = re.compile(r'''
        ::namedref::\s*\(\s*(\S+)\#(\w+)\s*\)
        '''
        , re.VERBOSE)
    BLOCK_RE2 = re.compile(r'''
        ::namedref::\s*\{\s*(\w+):([^}]+)\}
        ''', re.MULTILINE | re.DOTALL | re.VERBOSE)

    def __init__(self, md):
        super(MyPreprocessor, self).__init__(md)

    def run(self, lines):
        text = '\n'.join(lines)
        did_replace = True

        while did_replace:
            text, did_replace = self._replace_block(text)

        return text.split('\n')

    def _find_name(self, file, ref):
        txt = open("docs/"+file).read() # todo determine "docs" differently
        S = re.compile(r'''
            ::namedref::\s*\{\s*'''+ref+r''':([^}]+)\}
            ''', re.MULTILINE | re.DOTALL | re.VERBOSE)
        m = S.search(txt)
        if m:
            return m.group(1)
        else:
            #return "UNKNOWN"
            raise Exception("unknown reference: '{}#{}'".format(file,ref))


    def _replace_block(self, text):
        # Parse configuration params
        m = MyPreprocessor.BLOCK_RE.search(text)
        if m:
            name=self._find_name(m.group(1),m.group(2))
            output="[{}]({}#{})".format(name,m.group(1),m.group(2))
            return text[:m.start()] + output + text[m.end():], True

        m = MyPreprocessor.BLOCK_RE2.search(text)
        if m:
            output='<a name="{}"></a> {}'.format(m.group(1),m.group(2))
            return text[:m.start()] + output + text[m.end():], True

        return text, False


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
        md.preprocessors.add('namedref', blockprocessor, '_begin')


def makeExtension(*args, **kwargs):
    return MyMarkdownExtension(*args, **kwargs)
