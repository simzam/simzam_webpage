"""Models for simzam's homepage project.

All database models are contained in this file. This simplifies foreign keys
crossing files and lowers the complexities regarding migrating the database.

All tables are explictly named.

"""
from django.db import models
from django.contrib.admin.decorators import display
from django.utils.text import slugify
from django.utils.timezone import now
from django.template.loader import get_template
from tinymce import models as tinymce_models


class Project(models.Model):
    """A project is defined connected collection of elements of some sort."""

    title = models.CharField('tittel', unique=True, primary_key=True, max_length=255)
    description = tinymce_models.HTMLField('beskrivelse')

    created_date = models.DateField('opprettet', default=now)
    updated_date = models.DateField('oppdatert', default=now)

    project_states = (("SKETCHED", "På tapetet"),
                      ("TODO", "På bordet"),
                      ("HOLD", "I skuffen"),
                      ("DONE", "I arkivet"))
    state = models.CharField('tilstand', max_length=30, choices=project_states,
                             default="IDEA")

    slug = models.SlugField(max_length=255, blank=True, editable=False)
    logo = models.ImageField(upload_to='project_logos/', null=True, blank=True)
    #logo_t = models.ImageField(upload_to='project_logos_thumbnails/', null=True, blank=True)

    class Meta:
        """Sort projects by last updated project."""

        db_table = 'project'
        ordering = ['updated_date']

    @display(description='Preview')
    def show_logo(self):
        """Allow previewing of images on the admin page."""
        return get_template('admin/logo_thumbnail_template.html').render({
            'field_name': 'logo',
            'src': self.logo.url if self.logo else None,
        })

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super(Project, self).save(*args, **kwargs)


    def __str__(self):
        return self.title


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

    title = models.CharField('tittel', max_length=255)

    published_date = models.DateField('publisert', default=now)
    drawing = models.ImageField('Tegning', upload_to='drawing')

    # Add validator
    background_color = models.CharField(max_length=7, default="#FFFFFF")

    @display(description='Preview')
    def show_drawing(self):
        """Allow previewing of images on the admin page."""

        return get_template('admin/drawing_thumbnail_template.html').render({
            'field_name': 'drawing',
            'background_color': self.background_color,
            'src': self.drawing.url if self.drawing else None,
        })

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'drawing'
#         ordering =
#     @property
#     def thumnbail_preview(self):
#         if self.thumbnail:
#             url_string = '<img src="{}" width="300" height="300"/>'
#             returni mark_safe.format(url_string.format(self.thumbnail.url))
