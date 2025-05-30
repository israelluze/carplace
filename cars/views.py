from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm

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
    
def new_car_view(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()            
            return redirect('cars_list')  # Assuming you have a URL named 'cars_list'
    else:
        form = CarForm()
        return render(request, 'new_car.html', {'newcar_form': form, 'error': True})
    
       
    
    
