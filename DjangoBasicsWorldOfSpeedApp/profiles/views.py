from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from DjangoBasicsWorldOfSpeedApp.utils import get_user_obj
from profiles.forms import ProfileCreateForm, ProfileEditForm
from profiles.models import Profile


# Create your views here.


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile-create.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile-details.html'

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile-edit.html'
    success_url = reverse_lazy('profile-details')

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDeleteView(DeleteView):
    template_name = 'profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_user_obj()


