from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View
from django.views.generic import ListView,CreateView

class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'car_list'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            return super().get_queryset().filter(model__icontains=search).order_by('model')
        return cars  

class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'  # Redirect to the cars list after successful creation

    def form_valid(self, form):
        return super().form_valid(form)




