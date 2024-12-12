from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from DjangoTastyRecipesApp.utility import get_user_obj
from profiles.forms import ProfileCreateForm, ProfileEditForm
from profiles.models import Profile


# Create your views here.


class ProfileCreateView(CreateView):
    model = Profile
    template_name = "create-profile.html"
    form_class = ProfileCreateForm
    success_url = reverse_lazy('catalogue')


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'details-profile.html'

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'edit-profile.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('profile-details')

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDeleteView(DeleteView):
    template_name = 'delete-profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return get_user_obj()