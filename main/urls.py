from . import views
from django.urls import path
# urls.py

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='index'),
    path('dishes/<str:category_name>/', views.dishes_by_category, name='dishes_by_category'),
    path('dishes/', views.all_dishes, name='all_dishes'),
    path('dish/<int:id>/', views.dish_detail_view, name='dish_detail_view'),
    path('dish/create/', views.add_dish, name='add_dish'),
    path('dish/edit/<int:id>/', views.edit_dish, name='edit_dish'),
    path('add_to_favorites/<int:id>/', views.add_to_favorites, name='add_to_favorites'),
    path('favorite_dishes/', views.favorite_dishes, name='favorite_dishes'),

    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)