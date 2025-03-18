from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Item(models.Model):
    """ Model for Food Items """

    def __str__(self) -> str:
        return str(self.item_name)

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField(default=0)
    item_image = models.CharField(
        max_length=500,
        default='https://cdn.pixabay.com/photo/2017/02/16/02/54/coming-soon-2070393_1280.jpg')

    def get_absolute_url(self):
        """ Redirect to the detail page """
        return reverse('food:Detail', kwargs={'pk': self.pk})
