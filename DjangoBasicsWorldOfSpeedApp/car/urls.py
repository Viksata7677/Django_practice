from django.urls import path, include

from car import views

urlpatterns = [
    path('create/', views.CarCreateView.as_view(), name='create-car'),
    path('catalogue/', views.CarCatalogView.as_view(), name='catalogue'),
    path('<int:id>/', include([
                                path('details/', views.CarDetailView.as_view(), name='car-details'),
                                path('edit/', views.CarEditView.as_view(), name='car-edit'),
                                path('delete/', views.CarDeleteView.as_view(), name='car-delete'),
    ]))
]