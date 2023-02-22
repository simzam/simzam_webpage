from django.contrib import admin
from . models import Project
from . models import Drawing
# Register your models here.
from . forms import DrawingModelForm

admin.site.register(Project,
                    fields=('title',
                            'description',
                            'updated_date',
                            'show_logo',
                            'logo',
                            'created_date'),
                    readonly_fields=('show_logo',))

class ProjectAdmin(admin.ModelAdmin):
    exclude = ("slug",)

# @admin.register(Drawing)
class DrawingAdmin(admin.ModelAdmin):
    form = DrawingModelForm


admin.site.register(Drawing,
                    DrawingAdmin,
                    fields=('title',
                            'show_drawing',
                            'drawing',
                            'background_color'),
                    readonly_fields=('show_drawing',))
