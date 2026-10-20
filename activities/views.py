from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from activities.forms import ActivityCreateForm, ActivityCreateForm, ActivityEditForm, ActivityDeleteForm
from activities.models import Activity


# Create your views here.
def activity_view(request:HttpRequest):
    activities = Activity.objects.all()
    context = {'activities': activities}
    return render(request= request,
                  template_name="activities/activity_view.html",
                  context=context)

def activity_create_view(request:HttpRequest):
    form = ActivityCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('activities')
    context = {'form': form}
    return render(request= request,
                  template_name='activities/activity_create_view.html',
                  context=context
                  )

def activity_edit_view(request:HttpRequest, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    form=ActivityEditForm(request.POST or None,request.FILES or None, instance=activity)
    if form.is_valid():
        form.save()
        return redirect('activities')
    context = {'form': form}
    return render(request= request,
                  template_name='activities/activity_edit_view.html',
                  context=context)

def activity_detail_view(request:HttpRequest, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    context={'activity': activity}
    return render(request= request,
                  template_name='activities/activity_detail_view.html',
                  context=context)

def activity_delete_view(request:HttpRequest, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    form = ActivityDeleteForm(instance=activity)
    if request.method == 'POST':
        activity.delete()
        return redirect('activities')
    context = {'form': form,
               'activity': activity}
    return render(request= request,
                  template_name='activities/activity_delete_view.html',
                  context=context)