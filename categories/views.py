from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from categories.models import Category

# Create your views here.
class CategoryView(ListView):
    model = Category
    template_name = 'categories/category_list.html'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'categories/category_create.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('category_list')