"""Models for simzam's homepage project.

All database models are contained in this file. This simplifies foreign keys
crossing files and lowers the complexities regarding migrating the database.

All tables are explictly named.

"""


from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils.timezone import now
# from django.utils.html import mark_safe

class Project(models.Model):
    """A project is defined connected collection of elements of some sort."""

    title = models.CharField(max_length=255,
                             unique=True,
                             primary_key=True)
    description = models.TextField()
    published_date = models.DateField("date published", default=now)
    updated_date = models.DateField("last updated", default=now)

    project_states = (
        ("IDEA", "MEST I HODET"),
        ("SKETCHED", "PÅ TAPETET"),
        ("TODO", "PÅ BORDET"),
        ("HOLD", "I SKUFFEN")
        ("DONE", "I ARKIVET"))
    state = models.CharField(max_length=30, choices=project_states,
                             default="IDEA")

    test = models.TextField()
    slug = models.SlugField(blank=True)
    logo = models.ImageField(upload_to='project_logos/', null=True, blank=True)

    class Meta:
        """Sort projects by last updated project."""

        db_table = 'project'
        ordering = ['updated_date']

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# TODO: For project title is unique,
def pre_save_slug(instance, sender, *args, **kwargs):
    """Automatically generate slug."""
    instance.slug = slugify(instance.title)


pre_save.connect(pre_save_slug, sender=Project)


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


# class Drawing(models.Model):
#     """ A drawing contains a drawing in jpg format."""

#     title = models.CharField(max_length=255)

#     published_date = models.DateField("date published", default=now)
#     drawing = models.ImageField(upload_to='dd')
#     thumbnail = models.ImageField(upload_to='')

#     class Meta:
#         db_table = 'drawing'
#         ordering =

#     @property
#     def thumnbail_preview(self):
#         if self.thumbnail:
#             url_string = '<img src="{}" width="300" height="300"/>'
#             return mark_safe.format(url_string.format(self.thumbnail.url))
