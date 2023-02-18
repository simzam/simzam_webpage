from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from django.views.decorators.http import require_GET, require_POST
from django.urls import reverse
from datetime import datetime



# TODO: remove slug from argument list.
@require_GET
def detail(request: HttpRequest) -> HttpResponse:

    template = 'simzam/base.html'

    return render(request, template)
