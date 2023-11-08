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
        return render(request,'main/dish_form.html',{'form': DishForm()})
    elif request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'успішно доданий.')
            return redirect('index')
        else:
            messages.error(request, 'Помилки:')
            return render(request,'main/dish_form.html',{'form':form})
    
def edit_dish(request, id):
    dish = Dish.objects.filter(id = id)
    if request.method == 'GET':
        context = {'form': DishForm(instance=dish), 'id': id}
        return render(request,'main/dish_form.html',context)
    
    elif request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            messages.success(request, 'Дані про покупця успішно оновлено!')
            return redirect('index')
        else:
            messages.error(request, 'Помилка:')
            return render(request,'main/dish_form.html',{'form':form})
    