from django.urls import path
from activities import views

urlpatterns = [
    path('', views.activity_view, name='activities'),
    path('create/', views.activity_create_view, name='activity_create'),
]