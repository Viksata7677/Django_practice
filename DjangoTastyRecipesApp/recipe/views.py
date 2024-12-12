from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from DjangoTastyRecipesApp.utility import get_user_obj
from recipe.forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm
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


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'details-recipe.html'
    pk_url_kwarg = 'recipe_id'


class RecipeEditView(UpdateView):
    model = Recipe
    template_name = 'edit-recipe.html'
    success_url = reverse_lazy('catalogue')
    form_class = RecipeEditForm
    pk_url_kwarg = 'recipe_id'


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'delete-recipe.html'
    form_class = RecipeDeleteForm
    success_url = reverse_lazy('catalogue')
    pk_url_kwarg = 'recipe_id'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)
