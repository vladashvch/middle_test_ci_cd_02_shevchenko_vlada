from django.shortcuts import render, get_object_or_404
from .models import Recipe
import random

def main(request):
    recipes = list(Recipe.objects.all())
    random_recipes = random.sample(recipes, min(len(recipes), 10))
    return render(request, 'main.html', {'recipes': random_recipes})

