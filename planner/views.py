import random

from django.http import HttpRequest
from django.shortcuts import render

from activities.helpers import filter_activities
from activities.models import Activity
from planner.forms import ActivityPickerForm


# Create your views here.

def random_activity_view(request:HttpRequest):
    activities = Activity.objects.all()
    form=ActivityPickerForm(request.GET or None)
    selected_activity = None
    has_activities=Activity.objects.exists()
    if request.GET.get('pick')=='1' and form.is_valid():
        try:
            activities = filter_activities(activities, form.cleaned_data)
            selected_activity = random.choice(activities)

        except IndexError:
            selected_activity = None

    context = {
        'selected_activity': selected_activity,
        'has_picked': request.GET.get('pick')=="1",
        'form': form,
        'has_activities': has_activities,
    }

    return render(request,template_name="planner/random_activity_view.html",context=context)
