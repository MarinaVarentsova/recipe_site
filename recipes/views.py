from django.shortcuts import render, get_object_or_404, redirect  # Добавлен redirect для корректной работы
from .models import Recipe
from .forms import RecipeForm

def home(request):
    """
    Представление для отображения главной страницы.
    Выводит 5 случайных рецептов.
    """
    recipes = Recipe.objects.order_by('?')[:5]  # Используем случайный порядок для отображения рецептов
    return render(request, 'home.html', {'recipes': recipes})

def recipe_detail(request, id):
    """
    Представление для отображения подробной информации о рецепте.
    """
    recipe = get_object_or_404(Recipe, id=id)  # Получение рецепта по ID или возврат ошибки 404
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def add_recipe(request):
    """
    Представление для добавления нового рецепта.
    """
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)  # Создаем форму с данными из POST и файлами
        if form.is_valid():
            recipe = form.save(commit=False)  # Сохраняем данные формы без сохранения в базу
            recipe.author = request.user  # Устанавливаем текущего пользователя как автора
            recipe.save()  # Сохраняем объект рецепта
            form.save_m2m()  # Сохраняем поля ManyToMany (например, категории)
            return redirect('home')  # Перенаправляем на главную страницу
    else:
        form = RecipeForm()  # Если GET-запрос, создаем пустую форму
    return render(request, 'add_recipe.html', {'form': form})
