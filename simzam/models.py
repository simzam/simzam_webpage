"""Models for simzam's homepage project.

All database models are contained in this file. This simplifies foreign keys
crossing files and lowers the complexities regarding migrating the database.

All tables are explictly named.

"""
import uuid
from django.db import models
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.admin.decorators import display
from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import now
from django.template.loader import get_template
# from tinymce import models as tinymce_models

from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.conf import settings


# class Project(models.Model):
#     """A project is defined connected collection of elements of some sort."""

#     title = models.CharField('tittel', unique=True, primary_key=True, max_length=255)
#     # description = tinymce_models.HTMLField('beskrivelse')
#     description = models.TextField()

#     created_date = models.DateField('opprettet', default=now)
#     updated_date = models.DateField('oppdatert', default=now)

#     project_states = (("SKETCHED", "På tapetet"),
#                       ("TODO", "På bordet"),
#                       ("HOLD", "I skuffen"),
#                       ("DONE", "I arkivet"))
#     state = models.CharField('tilstand', max_length=30, choices=project_states,
#                              default="IDEA")

#     slug = models.SlugField(max_length=255, blank=True, editable=False)
#     logo = models.ImageField(upload_to='project_logos/', null=True, blank=True)

#     class Meta:
#         """Sort projects by last updated project."""

#         db_table = 'project'
#         ordering = ['updated_date']

#     @display(description='Preview')
#     def show_logo(self):
#         """Allow previewing of images on the admin page."""
#         return get_template('admin/drawing_thumbnail_template.html').render({

#             'field_name': 'logo',
#             'src': self.logo.url if self.logo else None,
#         })

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)

#         super(Project, self).save(*args, **kwargs)


#     def __str__(self):
#         return self.title


# class Entry(models.Model):
#     """An entry is text based blog entry."""

#     project = models.ForeignKey(Project, on_delete=models.PROTECT)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     published_date = models.DateField("date published", default=now)
#     slug = models.SlugField(blank=True)

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         self.project.updated_date = self.published_date

#         super(Entry, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.title


class Drawing(models.Model):
    """ A drawing contains a drawing in jpg format."""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField('tittel', max_length=255, blank=True)
    text = models.TextField()

    published_date = models.DateField('publisert', default=now)

    drawing = models.ImageField('Tegning', upload_to='drawing')

    small_image = models.ImageField('Liten tegning',
                                    upload_to='drawing/',
                                    blank=True)
    medium_image = models.ImageField('Medium tegning',
                                     upload_to='drawing',
                                     blank=True)
    large_image = models.ImageField('Stor tegning',
                                    upload_to='drawing',
                                    blank=True)


    # Add validator
    background_color = models.CharField(max_length=7, default="#FFFFFF")

    @display(description='Preview')
    def show_drawing(self):
        """Allow previewing of images on the admin page."""

        return get_template('admin/drawing_thumbnail_template.html').render({
            'field_name': 'drawing',
            'background_color': self.background_color,
            'src': self.drawing.url if self.medium_image else None,
        })

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'drawing'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Drawing, self).save(*args, **kwargs)

        if self.drawing:
            self.create_image_versions()

    def create_image_versions(self):
        with Image.open(self.drawing.path) as img:
            # Generate different versions of the image
            for version, size in settings.IMAGE_VERSIONS_SIZES.items():
                self.create_image_version(img, version, size)

    def create_image_version(self, img, version, size):
        img.thumbnail(size, Image.ANTIALIAS)
        buffer = BytesIO()
        img.save(buffer, 'JPEG')  # Change the format as needed (JPEG, PNG, etc.)
        buffer.seek(0)
        filename = f"{self.drawing.name.rsplit('.', 1)[0]}_{version}.jpg"
        print(filename)
        content_file = ContentFile(buffer.read())
        self.drawing.storage.save(filename, content_file)
        buffer.close()

        return filename


    # def get_absolute_url(self):
    #     return reverse('simzam:drawing-detail', kwargs={'uuid': self.id})
