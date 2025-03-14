""" This file is used to create the views for the food app. """


from django.shortcuts import render
from django.http import HttpResponse
from .models import Item


# Create your views here.


def index(request):

    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)


def item(request):
    """ This function is used to display the items. """

    return HttpResponse("<h1>Hello, world. You're at the polls item.</h1>")


def detail(request, item_id):
    """ This function is used to display the details of the item. """

    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }

    return render(request, 'food/detail.html', context)
