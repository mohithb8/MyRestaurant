from django.db import models


# Create your models here.
class Menu(models.Model):
    item=models.CharField(max_length=20)
    price=models.IntegerField()
    image=models.ImageField(upload_to="media")

    def __str__(self):
        return self.item
