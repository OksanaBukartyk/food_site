from . import views
from django.urls import path
# urls.py

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='index'),
    path('dishes/<str:category_name>/', views.dishes, name='dishes'),
    path('dish/<int:id>/', views.dish_detail_view, name='dish_detail_view'),
    path('dish/create/', views.add_dish, name='add_dish'),
    path('dish/edit/<int:id>/', views.edit_dish, name='edit_dish'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)