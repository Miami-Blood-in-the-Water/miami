from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.blocks import CharBlock, RichTextBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock


class IndexPage(Page):
    body = StreamField([
        ('heading', CharBlock(classname="full title")),
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]