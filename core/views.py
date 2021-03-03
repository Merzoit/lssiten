from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse, reverse_lazy

from .models import Order
from .forms import OrderForm

class IndexView(CreateView):
    model = Order
    template_name="index.html"
    form_class = OrderForm
    success_url = reverse_lazy("index")
    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Order.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)
