# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Event

# Create your views here.
def index(request):
    event_list = Event.objects.order_by('event_date')[:3]
    context = {'event_list': event_list}
    return render(request, 'PYNWsite/index.html', context)
#    return HttpResponse("Hello, World. You're at the PYNW index.")


