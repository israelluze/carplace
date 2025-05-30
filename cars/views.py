from django.shortcuts import render
from cars.models import Car

def cars_view(request): 
    
    search = request.GET.get('search')
    if search:
        car_list = Car.objects.filter(model__icontains=search).order_by('model')  
    else:
        car_list = Car.objects.all().order_by('model')
        
    print(car_list)
    return render(request, 'cars.html', {
        'car_list':car_list
    })
    
    
