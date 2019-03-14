from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Recipe


def recipes(request):
    recipe_list = Recipe.objects.order_by('-pub_date')
    paginator = Paginator(recipe_list, 8)

    page = request.GET.get('page')
    recipes = paginator.get_page(page)

    return render(request, 'recipes/recipes.html', {'recipes': recipes})


def recipe_detail(request, slug):
    detailrecipe = get_object_or_404(Recipe, slug=slug)
    return render(request, 'recipes/recipe_detail.html', {'recipe': detailrecipe})
