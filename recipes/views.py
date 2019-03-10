from django.shortcuts import render, get_object_or_404

from .models import Recipe


def recipes(request):
    recipes = Recipe.objects.order_by('-pub_date')
    return render(request, 'recipes/recipes.html', {'recipes': recipes})


def recipe_detail(request, slug):
    detailrecipe = get_object_or_404(Recipe, slug=slug)
    return render(request, 'recipes/recipe_detail.html', {'recipe': detailrecipe})
