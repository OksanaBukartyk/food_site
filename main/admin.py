from django.contrib import admin

# Register your models here.


from .models import Dish, Ingredient, Category

admin.site.register(Dish)
admin.site.register(Ingredient)
admin.site.register(Category)