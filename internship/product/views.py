from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class Product_list_View(LoginRequiredMixin,ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 5

class ProductDetailView(LoginRequiredMixin,DetailView):
    model = Product
