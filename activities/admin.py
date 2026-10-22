from django.contrib import admin

from activities.models import Activity
from categories.models import Category
from vibes.models import Vibe


# Register your models here.
@admin.register(Vibe)
class VibeAdmin(admin.ModelAdmin):
    ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    ...
