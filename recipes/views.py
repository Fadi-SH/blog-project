from django.shortcuts import render, get_object_or_404

from .models import Recipe


def recipes(request):
    recipes = Recipe.objects
    return render(request, 'recipes/recipes.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    detailrecipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': detailrecipe})
