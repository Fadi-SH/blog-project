from django.shortcuts import render
from weblog.models import Weblog
from recipes.models import Recipe
from projects.models import Project


def home(request):
    weblogs = Weblog.objects.order_by('-pub_date')[:3]
    recipes = Recipe.objects.order_by('-pub_date')[:3]
    projects = Project.objects.order_by('-pub_date')[:3]

    return render(request, 'home/home.html',
                  {'recipes': recipes, 'weblogs': weblogs, 'projects': projects})


def contact(request):
    return render(request, 'contact/contact.html')
