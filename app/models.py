from django.db import models

# Create your models here.


class Persion(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    code_melli = models.IntegerField(default=0, null=True, blank=True)
    # date = models.TimeField(format=None, input_formats=None)

    def __str__(self) :
        return self.last_name


class Cars(models.Model):
    name = models.CharField(max_length=100)
    model= models.CharField(max_length=30)

    # date = models.TimeField(default=None)

    def __str__(self) :
        return self.name



