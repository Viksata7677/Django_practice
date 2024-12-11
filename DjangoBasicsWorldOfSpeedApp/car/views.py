from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from DjangoBasicsWorldOfSpeedApp.utils import get_user_obj
from car.forms import CarCreateForm, CarEditForm, CarDeleteForm
from car.models import Car


# Create your views here.


def index_view(request):
    return render(request, 'index.html')


class CarCreateView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'car-create.html'
    success_url = reverse_lazy('catalogue')
    
    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class CarCatalogView(ListView):
    model = Car
    context_object_name = 'cars'
    template_name = 'catalogue.html'


class CarDetailView(DetailView):
    model = Car
    context_object_name = 'car'
    template_name = 'car-details.html'
    pk_url_kwarg = 'id'


class CarEditView(UpdateView):
    model = Car
    form_class = CarEditForm
    template_name = 'car-edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('catalogue')


class CarDeleteView(DeleteView):
    model = Car
    form_class = CarDeleteForm
    template_name = 'car-delete.html'
    success_url = reverse_lazy('catalogue')
    pk_url_kwarg = 'id'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)





