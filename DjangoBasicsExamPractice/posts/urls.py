from django.urls import path, include

from posts.views import CreatePostView, PostDetailView, PostEditView, PostDeleteView

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create-post'),
    path('<int:post_id>/', include([path('details/', PostDetailView.as_view(), name='details-view'),
                                    path('edit/', PostEditView.as_view(), name='edit-post'),
                                    path('delete/', PostDeleteView.as_view(), name='delete-post'),]))
]