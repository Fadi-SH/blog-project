from django.shortcuts import render, get_object_or_404
from .models import Project


def projects(request):
    projects = Project.objects
    return render(request, 'projects/projects.html', {'projects': projects})


def project_detail(request, project_id):
    detailproject = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/project_detail.html', {'project': detailproject})
