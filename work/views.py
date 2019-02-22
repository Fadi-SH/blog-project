from django.shortcuts import render
from .models import Work


def home(request):
    works = Work.objects
    return render(request, 'work/home.html', {'works': works})
