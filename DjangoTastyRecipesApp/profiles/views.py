from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from DjangoTastyRecipesApp.utility import get_user_obj
from profiles.forms import ProfileCreateForm
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