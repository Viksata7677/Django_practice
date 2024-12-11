
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from DjangoBasicsExamPractice.utils import get_user_obj
from posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from posts.models import Post


# Create your views here.

class DashboardView(ListView):
    model = Post
    template_name = 'dashboard.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()


class CreatePostView(CreateView):
    model = Post
    template_name = 'create-post.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'details-post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'posts'


class PostEditView(UpdateView):
    model = Post
    template_name = 'edit-post.html'
    pk_url_kwarg = 'post_id'
    form_class = PostEditForm
    context_object_name = 'posts'
    success_url = reverse_lazy('dashboard')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('dashboard')
    form_class = PostDeleteForm
    context_object_name = 'posts'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)








