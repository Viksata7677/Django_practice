from django.urls import path
from profiles.views import ProfileCreateView

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create-profile'),
]