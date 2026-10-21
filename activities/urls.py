from django.urls import path
from activities import views

urlpatterns = [
    path('',views.activity_view,name='activities'),
    path('create/',views.activity_create_view,name='activity_create'),
    path('edit/<int:activity_id>/',views.activity_edit_view,name='activity_edit'),
    path('details/<int:activity_id>/',views.activity_detail_view,name='activity_details'),
    path('delete/<int:activity_id>/',views.activity_delete_view,name='activity_delete'),
]