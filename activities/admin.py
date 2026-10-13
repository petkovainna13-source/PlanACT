from django.contrib import admin

from activities.models import Activity
from categories.models import Vibe, Category


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
