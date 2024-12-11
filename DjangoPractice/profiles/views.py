from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import BaseFormView, DeleteView
from album.models import Album
from profiles.forms import ProfileCreateForm
from DjangoPractice.utils import get_user_obj
from profiles.models import Profile


# Create your views here.


class HomePage(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')
    context_object_name = 'albums'

    def get_template_names(self):
        profile = get_user_obj()

        if profile:
            return ['home-with-profile.html']

        return ['home-no-profile.html']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['profile'] = get_user_obj()     # if profile in template
        return context
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileDetailView(DetailView):
    template_name = 'profile-details.html'

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDeleteView(DeleteView):
    template_name = 'profile-delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_user_obj()