from django import forms
from django.forms import HiddenInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML, Field, Hidden

from django.contrib.auth.models import User

from .models import SugarLevel, MealTime, CommonMeals


class SugarForm(forms.ModelForm):

    class Meta:
        model = SugarLevel
        fields = ['timestamp', 'sugar_level']

    def __init__(self, *args, **kwargs):
        super(SugarForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = False
        self.helper.layout = Layout(
            'timestamp',
            'sugar_level',
        )


class MealForm(forms.ModelForm):

    class Meta:
        model = MealTime
        fields = ['timestamp', 'meal_type', 'proteins', 'fat', 'carbohydrates', 'comments']

    def __init__(self, *args, **kwargs):
        super(MealForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = False
        self.helper.layout = Layout(
            'timestamp',
            'meal_type',
            'proteins',
            'fat',
            'carbohydrates',
            'comments',
        )


class CommonMealForm(forms.ModelForm):

    class Meta:
        model = CommonMeals
        fields = ['name', 'proteins', 'fat', 'carbohydrates', 'comments']

    def __init__(self, *args, **kwargs):
        super(CommonMealForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = False
        self.helper.layout = Layout(
            'name',
            'proteins',
            'fat',
            'carbohydrates',
            'comments',
        )
