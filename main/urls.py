from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'index'),
    path('dish/<int:id>/', views.dish_detail_view, name = 'dish_detail_view'),
    path('dish/create/', views.add_dish, name = 'add_dish'),
]