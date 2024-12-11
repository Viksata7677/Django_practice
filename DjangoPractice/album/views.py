from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from DjangoPractice.utils import get_user_obj
from album.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from album.models import Album


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class AlbumEditView(UpdateView):
    model = Album
    form_class = AlbumEditForm
    pk_url_kwarg = 'id'
    template_name = 'album-edit.html'
    success_url = reverse_lazy('home')


class AlbumDeleteView(DeleteView):
    model = Album
    form_class = AlbumDeleteForm
    pk_url_kwarg = 'id'
    template_name = 'album-delete.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class AlbumDetailsView(DetailView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'album-details.html'