from django.contrib import admin
from django.urls import path, include

from tracker import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_base),
    path('logout/', views.logout_base),
    path('sugar/new', views.add_sugar_level, name='add_sugar_level'),
    path('meal/new/', views.add_meal, name='add_meal'),
    # charts
    path('chart/levels', views.sugar_chart, name='sugar_chart'),
    # JSon Responses
    path('get/meal/<int:meal_id>/', views.get_meal_info, name='get_meal_info'),
]