from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Dish, Ingredient, Category, FavoriteDish
from .forms import DishForm, IngredientForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'main/index.html')


@login_required
def add_to_favorites(request, id):
    dish = get_object_or_404(Dish, pk=id)
    favorite_dish, created = FavoriteDish.objects.get_or_create(user=request.user)
    favorite_dish.favorite_dishes.add(dish)
    return render(request, 'main/index.html')

def dishes_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    subcategories = category.children.all()  # Отримати всі підкатегорії
    subcategories = subcategories | Category.objects.filter(pk=category.pk)  # Додати саму категорію до списку
    dishes = Dish.objects.filter(category__in=subcategories)
    return render(request, 'main/all_dishes.html', context={'dishes': dishes, 'category': category})

def favorite_dishes(request):
    if request.user.is_authenticated:
        favorite_dish, created = FavoriteDish.objects.get_or_create(user=request.user)
        favorite_dishes = favorite_dish.favorite_dishes.all()
        return render(request, 'main/all_dishes.html', {'dishes': favorite_dishes, 'title' :'Улюблені страви'})
    else:
        # Обробка випадку, коли користувач не аутентифікований
        return render(request, 'main/index.html')

def all_dishes(request):
    dishes = Dish.objects.all()
    return render(request, 'main/all_dishes.html', context={'dishes': dishes})

def dish_detail_view(request, id):
    dish = get_object_or_404(Dish, pk=id)
    is_favorite = False
    if request.user.is_authenticated:
        favorite_dish, created = FavoriteDish.objects.get_or_create(user=request.user)
        is_favorite = dish in favorite_dish.favorite_dishes.all()
    return render(request, 'main/dish.html', context={'dish': dish, 'is_favorite': is_favorite})

def add_dish(request):
    if request.method == 'GET':
        return render(request,'main/dish_form.html',{'form': DishForm()})
    elif request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            dish = form.save(commit=False)
            dish.save()
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
    