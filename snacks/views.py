from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Snack


class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack


class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack


class SnackCreateView(CreateView):
    template_name = 'snack_create.html'


class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'


class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'

