from django.db import models


class Crop(models.Model):
  name = models.CharField(max_length=64)
