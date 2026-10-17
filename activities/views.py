from django.http import HttpRequest
from django.shortcuts import render, redirect

from activities.forms import ActivityCreateForm, ActivityCreateForm
from activities.models import Activity


# Create your views here.
def activity_view(request:HttpRequest):
    activities = Activity.objects.all()
    context = {'activities': activities}
    return render(request= request,
                  template_name="activities/activity_view.html",
                  context=context)

def activity_create_view(request:HttpRequest):
    form = ActivityCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('activities')
    context = {'form': form}
    return render(request= request,
                  template_name='activities/activity_create_view.html',
                  context=context
                  )