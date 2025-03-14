""" This file is used to create the views for the food app. """

from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import Item


# Create your views here.


def index(request):

    iltem_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def item(request):
    return HttpResponse("<h1>Hello, world. You're at the polls item.</h1>")
