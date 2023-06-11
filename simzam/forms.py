#!/usr/bin/env python3
from django import forms
# from tinymce.widgets import TinyMCE
from django.forms import ModelForm
from .models import Project
#from .models import Drawing
from django.forms.widgets import TextInput


# class TinyMCEWidget(TinyMCE):
#  i   def use_required_attribute(self, *args):
#         return False


# class PostForm(forms.ModelForm):
#     content = forms.CharField(
#         widget=TinyMCEWidget(
#             attrs={'required': False, 'cols': 60, 'rows': 60}
#         )
#     )
#     class Meta:
#         model = Project
#         fields = '__all__'


class DrawingModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DrawingModelForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields["background_color"].widget = TextInput(
                attrs={"type": "color", "title": self.instance.background_color}
            )

    class Meta:
        widgets = {
            "background_color": TextInput(attrs={"type": "color"}),
        }
