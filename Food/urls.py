from django.urls import path
from . import views


# for Namespacing
app_name = 'food'


urlpatterns = [
    # food/
    path('', views.index, name='index'),

    # food/1/
    path('<int:item_id>/', views.detail, name='Detail'),
    path('item/', views.item, name='item'),

    # Add a Form
    path('add', views.create_item, name='create_item'),

    # Update a Form
    path('update/<int:id>/', views.update_item, name='update_item'),

    # Delete a item
    path('delete/<int:id>/', views.delete_item, name='delete_item'),

]
