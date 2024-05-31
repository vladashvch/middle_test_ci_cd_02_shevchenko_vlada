import pytest
from django.urls import reverse
from django.test import Client
from recipe.models import Recipe, Category

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def create_recipes():
    category = Category.objects.create(name="Dessert")
    recipes = [
        Recipe.objects.create(
            title=f"Recipe {i}",
            description="Description",
            instructions="Instructions",
            ingredients="Ingredients",
            category=category
        ) for i in range(10)
    ]
    return recipes

@pytest.mark.django_db
def test_main_view(client, create_recipes):
    url = reverse('main')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.context['recipes']) == 10

@pytest.mark.django_db
def test_category_detail_view(client, create_recipes):
    category = Category.objects.get(name="Dessert")
    url = reverse('category_detail', args=[category.id])
    response = client.get(url)
    assert response.status_code == 200
    assert 'category' in response.context
    assert response.context['category'] == category
    assert len(response.context['recipes']) == 10
    