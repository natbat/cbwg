from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    body = models.CharField(max_length=500, default='The California Bat Working Group (CBWG) is composed of individuals dedicated to bat research, education, management, and conservation. Our mission is to facilitate communication regarding bat ecology, distribution, and research techniques, and provide a forum to discuss conservation and management strategies, provide technical assistance, and encourage education.')
    updatesHeader = models.CharField(max_length=100, default='CBWG Updates')
    regionalHeader = models.CharField(max_length=100, default='Regional groups')
    initiativesHeader = models.CharField(max_length=100, default='Initiatives')

    intitiative1Title = models.CharField(max_length=250, blank=True, null=True)
    intitiative1Link = models.CharField(max_length=250, blank=True, null=True)
    intitiative1Body = RichTextField(blank=True, null=True)

    intitiative2Title = models.CharField(max_length=250, blank=True, null=True)
    intitiative2Link = models.CharField(max_length=250, blank=True, null=True)
    intitiative2Body = RichTextField(blank=True, null=True)

    intitiative3Title = models.CharField(max_length=250, blank=True, null=True)
    intitiative3Link = models.CharField(max_length=250, blank=True, null=True)
    intitiative3Body = RichTextField(blank=True, null=True)


    # TODO find a way to link to blog entries or static pages perhaps
    # and have them be overridable with header and intro

    subpage_types = ['blog.BlogIndexPage','home.StaticPage','blog.BlogTagIndexPage']

    content_panels = Page.content_panels + [
         FieldPanel('body', classname="full"),
         FieldPanel('updatesHeader', classname="full"),
         FieldPanel('regionalHeader', classname="full"),
         FieldPanel('initiativesHeader', classname="full"),

         FieldPanel('intitiative1Title', classname="full"),
         FieldPanel('intitiative1Link', classname="full"),
         FieldPanel('intitiative1Body', classname="full"),

         FieldPanel('intitiative2Title', classname="full"),
         FieldPanel('intitiative2Link', classname="full"),
         FieldPanel('intitiative2Body', classname="full"),

         FieldPanel('intitiative3Title', classname="full"),
         FieldPanel('intitiative3Link', classname="full"),
         FieldPanel('intitiative3Body', classname="full"),
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
