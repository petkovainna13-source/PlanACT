from django.http import HttpRequest
from django.shortcuts import render

from activities.models import Activity


# Create your views here.
def activity_view(request:HttpRequest):
    activities = Activity.objects.all()
    context = {'activities': activities}
    return render(request= request,
                  template_name="activities/activity_view.html",
                  context=context)
