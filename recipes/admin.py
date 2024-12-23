from django.contrib import admin
from .models import Recipe, Category  # Импорт обеих моделей


class RecipeAdmin(admin.ModelAdmin):
    exclude = ('author',)  # Исключить поле "Автор" из формы

    def save_model(self, request, obj, form, change):
        if not obj.author:  # Установить автора только если его нет
            obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)  # Регистрируем модель Categor

