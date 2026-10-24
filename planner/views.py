import random

from django.http import HttpRequest
from django.shortcuts import render

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
            budget = form.cleaned_data['budget']
            distance = form.cleaned_data['distance']
            pet_friendly = form.cleaned_data['pet_friendly']
            environment = form.cleaned_data['environment']

            if budget is not None:
                activities = activities.filter(budget__lte=budget)

            if distance is not None:
                activities = activities.filter(distance__lte=distance)

            if pet_friendly =="yes":

                activities = activities.filter(pet_friendly=True)
            elif pet_friendly =="no":
                activities = activities.filter(pet_friendly=False)

            if environment :
                activities = activities.filter(environment=environment)

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
