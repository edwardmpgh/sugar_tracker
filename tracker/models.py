from django.db import models
from django.db.models.functions import Lower
from django.conf import settings
from django.utils import timezone

DB_PREFIX = 'st_'


class CommonField(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    trash = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def is_active(self):
        return self.active

    def is_trash(self):
        return self.trash

    def flip_active_flag(self):
        if self.active:
            self.active = False
        else:
            self.active = True

    def flip_trash_flag(self):
        if self.trash:
            self.trash = False
        else:
            self.trash = True


class SugarLevel(CommonField):
    timestamp = models.DateTimeField(default=timezone.now())
    sugar_level = models.CharField(max_length=25, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = '%ssugar_level' % DB_PREFIX
        ordering = ['timestamp']

    def __str__(self):
        return '%s' % self.timestamp


MEAL_TYPES = [
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
    ('S', 'Snack'),
]


class MealTime(CommonField):
    timestamp = models.DateTimeField(default=timezone.now())
    meal_type = models.CharField(max_length=2, choices=MEAL_TYPES)
    fat = models.IntegerField(blank=True, null=True)
    carbohydrates = models.IntegerField(blank=True, null=True)
    proteins = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = '%smeal_type' % DB_PREFIX
        ordering = ['timestamp']

    def __str__(self):
        return '%s' % self.timestamp


class CommonMeals(CommonField):
    name = models.CharField(max_length=30)
    fat = models.IntegerField(blank=True, null=True)
    carbohydrates = models.IntegerField(blank=True, null=True)
    proteins = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = '%scommon_meals' % DB_PREFIX
        ordering = ['name']

    def __str__(self):
        return '%s' % self.name
