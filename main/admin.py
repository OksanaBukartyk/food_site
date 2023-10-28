from django.contrib import admin

# Register your models here.


from .models import Dish, Ingredient

admin.site.register(Dish)
admin.site.register(Ingredient)