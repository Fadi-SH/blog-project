from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Project


def projects(request):
    project_list = Project.objects.order_by('-pub_date')
    paginator = Paginator(project_list, 4)

    page = request.GET.get('page')
    projects = paginator.get_page(page)

    return render(request, 'projects/projects.html', {'projects': projects})


def project_detail(request, slug):
    detailproject = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/project_detail.html', {'project': detailproject})
