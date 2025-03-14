from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.


def index(request):

    iltem_list = Item.objects.all()

    return HttpResponse(iltem_list)


def item(request):
    return HttpResponse("<h1>Hello, world. You're at the polls item.</h1>")
