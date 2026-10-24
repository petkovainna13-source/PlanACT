from django.urls import path
from planner import views

urlpatterns = [
    path('',views.random_activity_view,name='random_activity'),]