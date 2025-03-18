from django.urls import path
from . import views


# for Namespacing
app_name = 'food'


urlpatterns = [
    # food/
    path('', views.IndexClassView.as_view(), name='index'),

    # food/1/
    path('<int:pk>/', views.FoodDetail.as_view(), name='Detail'),
    path('item/', views.item, name='item'),

    # Add a Form
    path('add', views.CreateItem.as_view(), name='create_item'),

    # Update a Form
    path('update/<int:id>/', views.update_item, name='update_item'),

    # Delete a item
    path('delete/<int:id>/', views.delete_item, name='delete_item'),

]
