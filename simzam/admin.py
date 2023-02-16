from django.contrib import admin
from . models import Project
# Register your models here.

admin.site.register(Project,
                    fields=('title',
                            'description',
                            'updated_date',
                            'show_drawing_thumbnail',
                            'logo',
                            'created_date'),
                    readonly_fields=('show_drawing_thumbnail',))

class ProjectAdmin(admin.ModelAdmin):
    exclude = ("slug",)
