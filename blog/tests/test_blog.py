from wagtail.test.utils import WagtailPageTestCase
from .models import BlogPostPage, BlogPageGalleryImage
from wagtail.images.models import Image
from wagtail.core.models import Page
from datetime import datetime


class BlogPostPageTestCase(WagtailPageTestCase):
    def setUp(self):
        self.blog_page = BlogPostPage.objects.create(
            title="Test Blog Post",
            blog_post_title="Test Blog Post Title",
            body="This is a test blog post.",
            date_published=datetime(2023, 11, 1),
        )

    def test_blog_page_creation(self):
        """
        Test that a BlogPostPage is created correctly.
        """
        self.assertEqual(self.blog_page.title, "Test Blog Post")
        self.assertEqual(self.blog_page.blog_post_title, "Test Blog Post Title")
        self.assertEqual(self.blog_page.body, "This is a test blog post.")
        self.assertEqual(self.blog_page.date_published, datetime(2023, 11, 1))


class BlogPageGalleryImageTestCase(WagtailPageTestCase):
    def setUp(self):
        self.blog_page = BlogPostPage.objects.create(
            title="Test Blog Post",
            blog_post_title="Test Blog Post Title",
            body="This is a test blog post.",
            date_published=datetime(2023, 11, 1),
        )

        self.image = Image.objects.create(
            title="Test Image",
            file="test-image.jpg",
        )

        self.gallery_image = BlogPageGalleryImage.objects.create(
            page=self.blog_page,
            image=self.image,
            caption="Test Image Caption",
        )

    def test_gallery_image_creation(self):
        """
        Test that a BlogPageGalleryImage is created correctly.
        """
        self.assertEqual(self.gallery_image.page, self.blog_page)
        self.assertEqual(self.gallery_image.image, self.image)
        self.assertEqual(self.gallery_image.caption, "Test Image Caption")
