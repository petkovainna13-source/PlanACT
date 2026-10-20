from django.urls import path
from .views import CategoryView, CategoryCreateView

urlpatterns = [
    path('', CategoryView.as_view(),name='category_list'),
    path('create/', CategoryCreateView.as_view(),name='category_create'),
]