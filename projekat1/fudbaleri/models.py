from django.db import models
from django.contrib.auth.models import User


class Fudbaler(models.Model):
    ime = models.CharField(max_length=30)
    prezime = models.CharField(max_length=30)
    godine = models.IntegerField(default=30)
    brojNaDresu = models.IntegerField(max_length=99)
    tim = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.prezime

    def is_popular(self):
        return self.godine > 5


