from django.urls import path, include

from recipe.views import CatalogPage, CreateRecipeView, RecipeDetailView, RecipeEditView, RecipeDeleteView

urlpatterns = [
    path('catalogue/', CatalogPage.as_view(), name='catalogue'),
    path('create/', CreateRecipeView.as_view(), name='create-recipe'),
    path('<int:recipe_id>/', include([
        path('details/', RecipeDetailView.as_view(), name='recipe-details'),
        path('edit/', RecipeEditView.as_view(), name='recipe-edit'),
        path('delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    ]))
]