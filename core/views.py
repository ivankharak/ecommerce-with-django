from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

# Create your views here.


class HomeView(ListView):
    model = Item
    template_name = "index.html"


def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "index.html", context)


class ItemDetailView(DetailView):
    model = Item
    template_name = "product-detail.html"


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "product-detail.html", context)
