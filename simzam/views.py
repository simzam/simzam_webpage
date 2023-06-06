"""Function views."""
from django.shortcuts import render
# from django.http import HttpRequest, HttpResponse
# from django.views.decorators.http import require_GET

# from django.shortcuts import get_object_or_404
# from django.shortcuts import get_list_or_404
# from django.core.paginator import Paginator
from django.views.generic import ListView
from django.views.generic import DetailView
from simzam.models import Drawing
from django.utils import timezone


class DrawingList(ListView):
    template_name = 'drawings.html'
    model = Drawing
    paginate_by = 10
    context_object_name = 'drawings'

    def get_template_names(self):
        if self.request.htmx:
            return 'partials/drawing-list.html'
        return 'drawings.html'

    def get_queryset(self):
        return Drawing.objects.all()


def drawing_partial(request):
    drawings = Drawing.objects.all()
    return render(request, 'partials/drawing-list.html', {'drawings': drawings})


class DrawingDetailView(DetailView):
    model = Drawing
    template_name = 'partials/drawing.html'
    context_object_name = 'drawing'

    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_template_names(self):
        if self.request.htmx:
            return 'partials/drawing-list.html'
        return 'drawings.html'
