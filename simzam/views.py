"""Function views."""
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_GET
from . models import Drawing
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.core.paginator import Paginator

# TODO Redesign of page!

@require_GET
def index(request: HttpRequest) -> HttpResponse:
    """Test view."""
    template = 'index.html'
    drawing_uuids = Drawing.objects.all()
    paginator = Paginator(drawing_uuids, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'drawings': page_obj}

    return render(request, template, context)


@require_GET
def drawing_index(request: HttpRequest) -> HttpRequest:
    """Show multiple drawings."""
    template = 'simzam/drawing_index.html'
    drawings = get_list_or_404(Drawing)
    context = {'drawings': drawings}

    return render(request, template, context)


@require_GET
def drawing_detail(request: HttpRequest, uuid: str) -> HttpRequest:
    """Show a drawing."""
    template = 'simzam/drawing_detail.html'
    selected = get_object_or_404(Drawing, id=uuid)
    context = {'title': selected.title,
               'url': selected.drawing.url}

    return render(request, template, context)
