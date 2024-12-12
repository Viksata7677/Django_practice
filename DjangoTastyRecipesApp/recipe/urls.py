from django.urls import path

from recipe.views import CatalogPage, CreateRecipeView

urlpatterns = [
    path('catalogue/', CatalogPage.as_view(), name='catalogue'),
    path('create/', CreateRecipeView.as_view(), name='create-recipe'),
]