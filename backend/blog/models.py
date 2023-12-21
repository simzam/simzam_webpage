from django.db import models
from wagtail import blocks
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    MultipleChooserPanel,
)
from wagtail.images.models import Image
from wagtail.images.blocks import ImageChooserBlock
from modelcluster.fields import ParentalKey


class ImageBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    image = ImageChooserBlock()
    alt = blocks.CharBlock(require=False)


class TextBlogBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(features=["h3", "bold", "italic", "link", "code"])


class BlogPostPage(Page):
    # Title of the blog post.
    # blog_post_title = models.CharField(max_length=200, blank=True)

    # Main content of the blog post.
    body = StreamField(
        [
            ("heading", blocks.CharBlock()),
            ("intro", TextBlogBlock(required=False, max_length=800)),
            ("image", ImageBlock(required=False)),
            ("text", TextBlogBlock(required=False)),
            ("images", blocks.ListBlock(ImageBlock, required=False)),
        ],
        blank=True,
        null=True,
        min_num=2,
        use_json_field=True,
    )
    # Date when the blog post was published.
    date_published = models.DateTimeField()

    content_panels = Page.content_panels + [
        FieldPanel("title"),
        FieldPanel("body", classname="full"),
        FieldPanel("date_published"),
    ]


class BlogIndexPage(Page):
    # Introduction for the blog index page.
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
    ]

    subpage_types = ["BlogPostPage", "BlogIndexPage"]

    def get_context(self, request):
        # Get the most recent blog posts.
        context = super().get_context(request)
        context["blog_posts"] = BlogPostPage.objects.live().order_by("-date_published")
        return context
