from django.contrib import admin

from .models import SugarLevel, MealTime, CommonMeals

admin.site.register(SugarLevel)
admin.site.register(MealTime)
admin.site.register(CommonMeals)
