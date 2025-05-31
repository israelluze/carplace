from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()            
            return redirect('login')  
    else:        
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars_list')
        # Se falhar, login_form já contém os erros
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('login')  # Redirect to login page after logout


