from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from DjangoBasicsExamPractice.utils import get_user_obj
from author.forms import AuthorCreateForm, AuthorEditForm
from author.models import Author


# Create your views here.


def index(request):
    user_obj = get_user_obj()
    return render(request, 'index.html', {'user_obj': user_obj})


class CreateAuthorView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'create-author.html'
    success_url = reverse_lazy('dashboard')


class AuthorDetailView(DetailView):
    template_name = 'details-author.html'
    context_object_name = 'author'

    def get_object(self, queryset=None):
        return get_user_obj()


class AuthorEditView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'edit-author.html'
    success_url = reverse_lazy('author-details')

    def get_object(self, queryset=None):
        return get_user_obj()


class AuthorDeleteView(DeleteView):
    template_name = 'delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_user_obj()


