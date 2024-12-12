from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from DjangoTastyRecipesApp.utility import get_user_obj
from recipe.forms import RecipeCreateForm
from recipe.models import Recipe


# Create your views here.


class CatalogPage(ListView):
    template_name = 'catalogue.html'
    queryset = Recipe.objects.all()


class CreateRecipeView(CreateView):
    model = Recipe
    template_name = "create-recipe.html"
    form_class = RecipeCreateForm
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)