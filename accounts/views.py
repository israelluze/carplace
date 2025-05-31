from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()            
            return redirect('cars_list')  
    else:        
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars_list')  # Redirect to the cars list after login
        else:
            error_message = "Invalid credentials"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')
    
