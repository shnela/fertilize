from django.db import models


# Fertilizer is a model for fertilizers products.
# later this model may be split for substance and product units available to buy
class Fertilizer(models.Model):
  name = models.CharField(max_length=64)
  volume = models.DecimalField(max_digits=6, decimal_places=2)  # in liters
  weight = models.DecimalField(max_digits=6, decimal_places=2)  # in kilograms
  price = models.DecimalField(max_digits=8, decimal_places=2,
                              null=True, blank=True)  # in PLN
  nutrients = models.ManyToManyField('nutrients.Nutrient',
                                     through='NutrientContent')

  def __str__(self):
    return self.name


class NutrientContent(models.Model):
  nutrient = models.ForeignKey('nutrients.Nutrient', on_delete=models.PROTECT)
  fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
  percentage_content = models.DecimalField(max_digits=5, decimal_places=2)
  
  class Meta:
     unique_together = ('nutrient', 'fertilizer')

  def __str__(self):
    return '{0} - {1}% {2}'.format(self.fertilizer.name,
                                   self.percentage_content,
                                   self.nutrient)
