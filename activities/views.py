from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from activities.forms import (ActivityCreateForm, ActivityCreateForm,
                              ActivityEditForm, ActivityDeleteForm, ActivityFilterForm)
from activities.helpers import filter_activities
from activities.models import Activity


# Create your views here.
def activity_view(request:HttpRequest):
    has_activities=Activity.objects.exists()
    activities=Activity.objects.all()
    form=ActivityFilterForm(request.GET or None)

    if form.is_valid():
        activities = filter_activities(activities, form.cleaned_data)

        min_budget = form.cleaned_data['min_budget']
        if min_budget is not None:
            activities = activities.filter(budget__gte=min_budget)

        sort=form.cleaned_data['sort']
        if sort:
            activities = activities.order_by(sort)
    elif form.is_bound:
        activities=Activity.objects.none()


    context={'activities': activities,
             'form':form,
             'has_activities':has_activities,}
    return render(request= request,
                  template_name="activities/activity_view.html",
                  context=context)

def activity_create_view(request:HttpRequest):
    form=ActivityCreateForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('activities')
    context={'form':form}
    return render(request=request,
                  template_name='activities/activity_create_view.html',
                  context=context
                  )

def activity_edit_view(request:HttpRequest, activity_id):
    activity=get_object_or_404(Activity,id=activity_id)
    form=ActivityEditForm(request.POST or None,request.FILES or None,instance=activity)
    if form.is_valid():
        form.save()
        return redirect('activities')
    context={'form':form}
    return render(request=request,
                  template_name='activities/activity_edit_view.html',
                  context=context)

def activity_detail_view(request:HttpRequest, activity_id):
    activity=get_object_or_404(Activity, id=activity_id)
    context={'activity': activity}
    return render(request=request,
                  template_name='activities/activity_detail_view.html',
                  context=context)

def activity_delete_view(request:HttpRequest, activity_id):
    activity=get_object_or_404(Activity,id=activity_id)
    form=ActivityDeleteForm(instance=activity)
    if request.method=='POST':
        activity.delete()
        return redirect('activities')
    context={'form':form,
               'activity':activity}
    return render(request=request,
                  template_name='activities/activity_delete_view.html',
                  context=context)