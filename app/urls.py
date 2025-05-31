from django.contrib import admin
from django.urls import path
from accounts.views import register_view, login_view
from app import settings
from django.conf.urls.static import static
from cars.views import cars_view, new_car_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),  # Assuming you have a registration view
    path('login/', login_view, name='login'),  # Using Django's built-in login view
    path('cars/', cars_view, name='cars_list'),  # Include the URLs from the cars app
    path('new_car/', new_car_view, name='new_car'),  # Assuming you have a view for adding new cars
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

