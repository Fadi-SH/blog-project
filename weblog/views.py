from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Weblog


def weblog(request):
    weblog_list = Weblog.objects.order_by('-pub_date')
    paginator = Paginator(weblog_list, 8)

    page = request.GET.get('page')
    weblogs = paginator.get_page(page)

    return render(request, 'weblog/weblog.html', {'weblogs': weblogs})


def weblog_detail(request, slug):
    detailweblog = get_object_or_404(Weblog, slug=slug)
    return render(request, 'weblog/weblog_detail.html', {'weblog': detailweblog})
