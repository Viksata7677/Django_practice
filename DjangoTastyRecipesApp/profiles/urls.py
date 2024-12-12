from django.urls import path
from profiles.views import ProfileCreateView, ProfileDetailView

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create-profile'),
    path('details/', ProfileDetailView.as_view(), name='profile-details'),
]