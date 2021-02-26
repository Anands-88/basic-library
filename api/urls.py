from django.urls import path
from .views import BookAPIView, CarAPIView

urlpatterns = [
    path('book/',BookAPIView.as_view()),
    path('car',CarAPIView.as_view()),
]
