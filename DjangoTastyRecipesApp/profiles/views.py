from django.urls import reverse_lazy
from django.views.generic import CreateView
from profiles.forms import ProfileCreateForm
from profiles.models import Profile


# Create your views here.


class ProfileCreateView(CreateView):
    model = Profile
    template_name = "create-profile.html"
    form_class = ProfileCreateForm
    success_url = reverse_lazy('catalogue')
