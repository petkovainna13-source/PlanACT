# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from vibes.models import Vibe

class VibesView(ListView):
    model=Vibe
    template_name = 'vibes/vibe_list.html'

class VibeCreateView(CreateView):
    model=Vibe
    template_name='vibes/vibe_create.html'
    fields=['name']
    success_url=reverse_lazy('vibe_list')

class VibeEditView(UpdateView):
    model=Vibe
    fields=['name']
    template_name = 'vibes/vibe_edit.html'
    success_url=reverse_lazy('vibe_list')

class VibeDeleteView(DeleteView):
    model=Vibe
    template_name = 'vibes/vibe_delete.html'
    success_url=reverse_lazy('vibe_list')