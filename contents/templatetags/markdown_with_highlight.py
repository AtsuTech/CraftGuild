from django import template
from django.template.defaultfilters import stringfilter
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.toc import TocExtension
from markdown.extensions.sane_lists import SaneListExtension
from markdown.extensions.nl2br import Nl2BrExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.wikilinks import WikiLinkExtension
from markdown.extensions.footnotes import FootnoteExtension
from markdown.extensions.tables import TableExtension




register = template.Library()





@register.filter
@stringfilter
def markdown_with_highlight(value):
    extensions = [
        CodeHiliteExtension(),
        TocExtension(marker="[TOC]"),
        SaneListExtension(),
        Nl2BrExtension(),
        FencedCodeExtension(),
        WikiLinkExtension(base_url="/wiki/", end_url=".html"),
        FootnoteExtension(),
        TableExtension(),
        'fenced_code', 
        'codehilite',
    ]

    #html_output = "s"

    # for md in mds:
    # if print('```' in value):
    #     conv1 = value.replace(':', '<span class="md-title">')
    #     conv2 = conv1.replace(';', '</span>')
        
    # html_output = conv2

    html_output = markdown.markdown(value, extensions=extensions)
    return(html_output)