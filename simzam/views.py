from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from django.views.decorators.http import require_GET, require_POST
from django.urls import reverse
from datetime import datetime


@require_GET
def detail(request: HttpRequest) -> HttpResponse:

    template = 'simzam/base.html'
    context = {}

    return render(request, template, context)

@require_GET
def drawing_index(request: HttpRequest) -> HttpRequest:

    template = 'simzam/drawing_index.html'
    context = {}

    return render(request, template, context)
