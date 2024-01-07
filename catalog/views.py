from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView, ListView, DeleteView, DetailView

from catalog.models import Product, Category


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Главная страница',
    }
    template_name = 'catalog/index.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты',
    }


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'price', 'image', 'category')
    success_url = reverse_lazy('catalog:base')


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'Товар',
    }
    template_name = 'catalog/product_detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'price', 'image', 'category')
    success_url = reverse_lazy('catalog:base')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
