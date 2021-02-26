from django.urls import path
from .views import CarsView

urlpatterns = [
    path('car',CarsView.as_view(), name='car')
]