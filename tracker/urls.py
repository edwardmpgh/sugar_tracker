from django.contrib import admin
from django.urls import path, include

from tracker import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_base),
    path('logout/', views.logout_base),
    path('sugar/new', views.add_sugar_level, name='add_sugar_level'),
    path('meal/new/', views.add_meal, name='add_meal'),
]
