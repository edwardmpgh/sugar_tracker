from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
from django.db import connections

from .models import SugarLevel, MealTime
from .forms import SugarForm, MealForm

SYSTEM_TITLE = 'Diabetes Tracker'


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

    return render(request, 'tracker/generic_form.html', context)
