from django import forms
from .models import Dish, Ingredient

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['title', 'image', 'description', 'time', 'complexity',
                  'portions', 'video_url']  # List the fields you want to edit


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['title', 'count', 'variable'] 

