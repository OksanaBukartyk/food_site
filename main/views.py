from django.shortcuts import render, redirect, get_object_or_404
from .models import Dish, Ingredient
from .forms import DishForm, IngredientForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'main/index.html', context={'dishes': Dish.objects.all()})

def dish_detail_view(request, id):
    return render(request, 'main/dish.html', context={'dish': Dish.objects.filter(id = id)})

def add_dish(request):
    if request.method == 'GET':
        return render(request,'main/add_item.html',{'form': DishForm()})
    elif request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'успішно доданий.')
            return redirect('index')
        else:
            messages.error(request, 'Помилки:')
            return render(request,'main/add_item.html',{'form':form})
    