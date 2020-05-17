from django.contrib import admin
from django.urls import path, include

from tracker import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_base),
    path('logout/', views.logout_base),
    path('sugar/new', views.add_sugar_level, name='add_sugar_level'),
    path('meal/new/', views.add_meal, name='add_meal'),
    path('meal/common/new', views.add_common_meal, name='add_common_meal'),
    # charts
    path('chart/sugar', views.sugar_graph, name='sugar_graph'),
    path('chart/meal', views.meal_graph, name='meal_graph'),
    path('chart/meal-sugar', views.meal_sugar_graph, name='meal_sugar_graph'),
    # charts API
    path('api/chart/levels', views.sugar_chart, name='sugar_chart'),
    path('api/chart/meals', views.meal_chart, name='meal_chart'),
    path('api/chart/mix', views.mix_chart, name='mix_chart'),
    # JSon Responses
    path('get/meal/<int:meal_id>/', views.get_meal_info, name='get_meal_info'),
]
