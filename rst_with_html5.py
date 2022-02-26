"""
author: @cwittlut <i@bitbili.net>
"""
import os
from pelican import readers, signals
from docutils.writers.html5_polyglot import HTMLTranslator, Writer

class _FieldBodyTranslator(HTMLTranslator):

    def __init__(self, document):
        super().__init__(document)
        self.compact_p = None

    def astext(self):
        return ''.join(self.body)

    def visit_field_body(self, node):
        pass

    def depart_field_body(self, node):
        pass

class PelicanHTMLTranslator(HTMLTranslator):

    def visit_abbreviation(self, node):
        attrs = {}
        if node.hasattr('explanation'):
            attrs['title'] = node['explanation']
        self.body.append(self.starttag(node, 'abbr', '', **attrs))

    def depart_abbreviation(self, node):
        self.body.append('</abbr>')

    def visit_literal_block(self, node):
        self.body.append(self.starttag(node, 'pre', '', CLASS='literal-block'))
        self.body.append('<code>')

    def depart_literal_block(self, node):
        self.body.append('</code>')
        self.body.append('</pre>\n')

    def visit_image(self, node):
        # set an empty alt if alt is not specified
        # avoids that alt is taken from src
        node['alt'] = node.get('alt', '')
        return HTMLTranslator.visit_image(self, node)

class PelicanHTMLWriter(Writer):

    def __init__(self):
        super().__init__()
        self.translator_class = PelicanHTMLTranslator

def replace_classes(readers):
    readers.reader_classes['rst'].writer_class = PelicanHTMLWriter
    readers.reader_classes['rst'].field_body_translator_class = _FieldBodyTranslator

def register():
    signals.readers_init.connect(replace_classes)
