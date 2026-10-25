import random

from django import template
from django.shortcuts import render

from activities.models import Activity

register = template.Library()

@register.filter
def budget_label(budget):
    if budget ==0:
        result= 'Free'
    elif 0<budget<=20:
        result = 'Budget-friendly'
    elif 20<budget<=100:
        result = 'Moderate'
    elif budget>100:
        result = 'Expensive'
    return result

@register.simple_tag
def featured_activity():
    activities = Activity.objects.all()
    try:
        selected_activity = random.choice(activities)

    except IndexError:
        selected_activity = None

    return selected_activity