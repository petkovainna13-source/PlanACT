from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from categories.models import Category

# Create your views here.
class CategoryView(ListView):
    model=Category
    template_name='categories/category_list.html'

class CategoryCreateView(CreateView):
    model=Category
    template_name='categories/category_create.html'
    fields=['name','description']
    success_url=reverse_lazy('category_list')

class CategoryEditView(UpdateView):
    model=Category
    template_name='categories/category_edit.html'
    fields=['name','description']
    success_url=reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model=Category
    template_name = 'categories/category_delete.html'
    success_url=reverse_lazy('category_list')

    def form_valid(self,form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.error(self.request,'You cannot delete this category '
                                        'while it belongs to exising activities')
            return redirect('category_list')