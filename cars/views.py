from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm

def cars_view(request): 
    
    search = request.GET.get('search')
    if search:
        car_list = Car.objects.filter(model__icontains=search).order_by('model')  
    else:
        car_list = Car.objects.all().order_by('model')        
    
    return render(request, 'cars.html', {
        'car_list':car_list
    })
    
def new_car_view(request):
    if request.method == "POST":
        form = CarModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars_list')  # Assuming you have a URL named 'cars_list'
        # Se não for válido, cai aqui e renderiza o formulário com erros
    else:
        form = CarModelForm()
    return render(request, 'new_car.html', {'newcar_form': form})




