from django import forms
from .models import Recipe, Category

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'steps', 'cooking_time', 'image', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple()  # Отображение категорий в виде чекбоксов
        }
