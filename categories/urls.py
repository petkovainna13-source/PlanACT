from django.urls import path
from .views import CategoryView, CategoryCreateView, CategoryEditView, CategoryDeleteView

urlpatterns = [
    path('',CategoryView.as_view(),name='category_list'),
    path('create/',CategoryCreateView.as_view(),name='category_create'),
    path('edit/<int:pk>/',CategoryEditView.as_view(),name='category_edit'),
    path('delete/<int:pk>/',CategoryDeleteView.as_view(),name='category_delete'),
]