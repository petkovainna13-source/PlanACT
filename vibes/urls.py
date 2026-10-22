from django.urls import path
from .views import VibesView, VibeCreateView, VibeEditView, VibeDeleteView

urlpatterns = [
    path('',VibesView.as_view(),name='vibe_list'),
    path('create/',VibeCreateView.as_view(),name='vibe_create'),
    path('edit/<int:pk>/',VibeEditView.as_view(),name='vibe_edit'),
    path('delete/<int:pk>/',VibeDeleteView.as_view(),name='vibe_delete')
]
