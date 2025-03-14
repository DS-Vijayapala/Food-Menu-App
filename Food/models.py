from django.db import models

# Create your models here.


class Item(models.Model):
    """ Model for Food Items """

    def __str__(self) -> str:
        return str(self.item_name)

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField(default=0)
    item_image = models.CharField(
        max_length=500,
        default='https://cdn.pixabay.com/photo/2017/02/16/02/54/coming-soon-2070393_1280.jpg')
