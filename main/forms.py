from django import forms
from .models import Dish, Ingredient, Category

class DishForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(parent__isnull=True))
    class Meta:
        model = Dish
        fields = ['title', 'image', 'description', 'time', 'complexity',
                  'portions', 'video_url', 'category']  # List the fields you want to edit
        



class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['title', 'count', 'variable'] 

