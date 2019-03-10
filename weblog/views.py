from django.shortcuts import render, get_object_or_404

from .models import Weblog


def weblog(request):
    weblogs = Weblog.objects.order_by('-pub_date')
    return render(request, 'weblog/weblog.html', {'weblogs': weblogs})


def weblog_detail(request, slug):
    detailweblog = get_object_or_404(Weblog, slug=slug)
    return render(request, 'weblog/weblog_detail.html', {'weblog': detailweblog})
