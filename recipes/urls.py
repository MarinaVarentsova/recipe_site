from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Главная страница
    path('', views.home, name='home'),
    
    # Детализация рецепта
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    
    # Добавление рецепта
    path('add/', views.add_recipe, name='add_recipe'),
    
    # Регистрация
    path('register/', auth_views.LoginView.as_view(template_name='registration/register.html'), name='register'),
    
    # Авторизация
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # Выход из системы
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]



