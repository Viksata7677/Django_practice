from django.urls import path

from author.views import CreateAuthorView, AuthorDetailView, AuthorEditView, AuthorDeleteView

urlpatterns = [
    path('create/', CreateAuthorView.as_view(), name='create-author'),
    path('details/', AuthorDetailView.as_view(), name='author-details'),
    path('edit/', AuthorEditView.as_view(), name='author-edit'),
    path('delete/', AuthorDeleteView.as_view(), name='author-delete'),
]