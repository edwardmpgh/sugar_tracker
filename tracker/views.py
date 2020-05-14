from datetime import datetime

from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
from django.db import connections
from django.conf import settings
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.db.models import Sum
from django.http import JsonResponse

from .models import SugarLevel, MealTime, CommonMeals
from .forms import SugarForm, MealForm

SYSTEM_TITLE = 'Diabetes Tracker'


def login_base(request):
    next = request.GET.get('next', '/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "users/login.html", {'redirect_to': next})


def logout_base(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)


@login_required
def sugar_chart(request):
    current_user = request.user
    levels = SugarLevel.objects.filter(trash=False, active=True, user=current_user)
    labels = []
    data = []
    for entry in levels:
        labels.append(entry.timestamp)
        data.append(entry.sugar_level)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


@login_required
def index(request):

    current_user = request.user

    context = dict(title=SYSTEM_TITLE,
                   page='index',
                   app_page='tracker',
                   fullname=current_user.first_name + ' ' + current_user.last_name,
                   )

    return render(request, 'tracker/index.html', context)


@login_required
def add_sugar_level(request):

    current_user = request.user

    context = dict(title=SYSTEM_TITLE,
                   page='index',
                   app_page='sugar',
                   fullname=current_user.first_name + ' ' + current_user.last_name,
                   )

    form = SugarForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            f = form.save(commit=False)
            f.user = current_user
            form.save()
            return HttpResponseRedirect(reverse('index'))

    context['form'] = form
    context['form_title'] = 'Add Sugar Level'
    context['button_title'] = 'Add'

    return render(request, 'tracker/generic_form.html', context)


@login_required
def add_meal(request):

    current_user = request.user

    context = dict(title=SYSTEM_TITLE,
                   page='index',
                   app_page='meal',
                   fullname=current_user.first_name + ' ' + current_user.last_name,
                   )

    form = MealForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            f = form.save(commit=False)
            f.user = current_user
            form.save()
            return HttpResponseRedirect(reverse('index'))

    context['form'] = form
    context['form_title'] = 'Add Meal'
    context['button_title'] = 'Add'
    context['common_meals'] = CommonMeals.objects.filter(trash=False, active=True, user=current_user)
    return render(request, 'tracker/meal_form.html', context)


@login_required
def get_meal_info(request, meal_id):

    meal = get_object_or_404(CommonMeals, id=meal_id)

    return JsonResponse(data={
        'fat': meal.fat,
        'carbohydrates': meal.carbohydrates,
        'protein': meal.proteins,
    })