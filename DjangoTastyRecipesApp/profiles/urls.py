from django.urls import path
from profiles.views import ProfileCreateView, ProfileDetailView, ProfileEditView

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create-profile'),
    path('details/', ProfileDetailView.as_view(), name='profile-details'),
    path('edit/', ProfileEditView.as_view(), name='profile-edit'),
]