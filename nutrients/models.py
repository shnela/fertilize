from django.db import models


class Nutrient(models.Model):
  name = models.CharField(max_length=128, unique=True)
  abbreviation = models.CharField(max_length=16, unique=True,
                                  null=True, blank=True)

  def __str__(self):
    str_name = self.name
    if self.abbreviation is not None:
      str_name = '{0} ({1})'.format(self.name, self.abbreviation)
    return str_name
