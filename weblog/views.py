from django.shortcuts import render, get_object_or_404

from .models import Weblog


def weblog(request):
    weblog = Weblog.objects
    return render(request, 'weblog/weblog.html', {'weblog': weblog})


def weblog_detail(request, slug):
    detailweblog = get_object_or_404(Weblog, slug=slug)
    return render(request, 'weblog/weblog_detail.html', {'weblog': detailweblog})
