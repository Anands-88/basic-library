from django.views.generic import ListView
from .models import Car

class CarsView(ListView):
    model = Car
    template_name = 'car_list.html'

