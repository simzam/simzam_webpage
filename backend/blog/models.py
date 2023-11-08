from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    MultipleChooserPanel,
)
from wagtail.images.models import Image
from modelcluster.fields import ParentalKey


class BlogPostPage(Page):
    # Title of the blog post.
    blog_post_title = models.CharField(max_length=200, blank=True)

    # Main content of the blog post.
    body = RichTextField(blank=True)

    # Date when the blog post was published.
    date_published = models.DateTimeField()

    # Featured image for the blog post.

    content_panels = Page.content_panels + [
        FieldPanel("title"),
        FieldPanel("body", classname="full"),
        FieldPanel("date_published"),
        MultipleChooserPanel(
            "gallery_images",
            label="Gallery images",
            chooser_field_name="image",
        ),
    ]


class ReceipePostPage(Page):
    # Title of the blog post.
    blog_post_title = models.CharField(max_length=200, blank=True)

    # Main content of the blog post.
    body = RichTextField(blank=True)

    # Date when the blog post was published.
    date_published = models.DateTimeField()

    # Featured image for the blog post.

    content_panels = Page.content_panels + [
        FieldPanel("title"),
        FieldPanel("body", classname="full"),
        FieldPanel("date_published"),
    ]


class BlogPageGalleryImage(Orderable):
    """
    Example related image
    """

    page = ParentalKey(
        BlogPostPage, on_delete=models.CASCADE, related_name="gallery_images"
    )
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel("image"),
        FieldPanel("caption"),
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
        blog_posts = BlogPostPage.objects.live().order_by("-date_published")
        return {
            "blog_posts": blog_posts,
        }
