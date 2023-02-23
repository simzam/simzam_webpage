"""Function views."""
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_GET
from . models import Drawing
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404


@require_GET
def detail(request: HttpRequest) -> HttpResponse:
    """Test view."""
    template = 'simzam/base.html'
    context = {}

    return render(request, template, context)


@require_GET
def drawing_index(request: HttpRequest) -> HttpRequest:
    """Show multiple drawings."""
    template = 'simzam/drawing_index.html'
    drawings = get_list_or_404(Drawing)
    context = {'drawings': drawings}

    return render(request, template, context)


@require_GET
def drawing_detail(request: HttpRequest, slug: str) -> HttpRequest:
    """Show a drawing."""
    template = './drawing_detail.html'
    drawing = get_object_or_404(Drawing, slug=slug)
    context = {'drawing': drawing}

    return render(request, template, context)


@require_GET
def memo(request: HttpRequest) -> HttpRequest:
    return render(request, './simzam/memo.html')
