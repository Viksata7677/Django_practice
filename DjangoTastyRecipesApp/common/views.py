from django.views.generic import TemplateView


# Create your views here.


class HomePage(TemplateView):
    template_name = "home-page.html"
