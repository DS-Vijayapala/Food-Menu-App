""" This file is used to create the views for the food app. """

from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item


# Create your views here.


# def index(request): # This is a function based view

#     item_list = Item.objects.all()
#     context = {
#         'item_list': item_list,
#     }
#     return render(request, 'food/index.html', context)


class IndexClassView(ListView):
    """ This class is used to display the items.  This is a class based view. """
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


def item(request):
    """ This function is used to display the items. """

    return HttpResponse("<h1>Hello, world. You're at the polls item.</h1>")


# def detail(request, item_id):
#     """ This function is used to display the details of the item. """

#     item = Item.objects.get(pk=item_id)
#     context = {
#         'item': item,
#     }

#     return render(request, 'food/detail.html', context)


class FoodDetail(DetailView):
    """ This class is used to display the details of the item. """

    model = Item
    template_name = 'food/detail.html'


# def create_item(request):
#     """ This function is used to create the item. """

#     form = ItemForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect('food:index')

#     context = {
#         'form': form,
#     }

#     return render(request, 'food/item-form.html', context)

class CreateItem(CreateView):
    """ This class is used to create the item. """

    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


def update_item(request, id):
    """ This function is used to update the item. """

    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {
        'form': form,
        'item': item,
    }

    return render(request, 'food/item-form.html', context)


def delete_item(request, id):
    """ This function is used to delete the item. """

    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    context = {
        'item': item,
    }

    return render(request, 'food/delete-item.html', context)
