from django.db import models

# Create your models here.


class cmdr(models.Model):
    Text=models.TextField()


    def __str__(self):
        return self.Text
