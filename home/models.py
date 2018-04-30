from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    subpage_types = ['blog.BlogIndexPage','home.StaticPage','blog.BlogTagIndexPage']

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    def get_updates(self):
        p = Page.objects.get(slug='updates')
        return p.get_descendants().order_by('-blogpage__date')[:3]


class StaticPage(Page):
    body = RichTextField(blank=True)

    parent_page_types = ['home.HomePage', 'home.StaticPage']
    subpage_types = ['home.StaticPage']

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
