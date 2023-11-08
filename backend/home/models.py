from django.db import models

from wagtail.search import index
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    max_count = 1


class AboutPage(Page):
    # Title field is inherited from Page

    # Add fields specific to the "About" page
    body = RichTextField(
        verbose_name="About Text",
        blank=True,
    )

    profile_banner = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Profile Banner",
        help_text="Upload your profile banner (PNG image) here.",
    )

    profile_photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Profile Photo",
        help_text="Upload your profile photo here.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("body", classname="full"),
        FieldPanel("profile_banner"),
        FieldPanel("profile_photo"),
    ]

    parent_page_types = ["home.HomePage"]

    max_count = 1

    search_fields = Page.search_fields + [
        index.SearchField("body"),
    ]
