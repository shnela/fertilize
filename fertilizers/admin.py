from django.contrib import admin

from fertilizers.models import (
  Fertilizer,
  NutrientContent,
)


class FertilizerAdmin(admin.ModelAdmin):
  list_display = ('name', 'volume', 'weight', 'price')


class NutrientContentaAdmin(admin.ModelAdmin):
  list_display = ('fertilizer', 'percentage_content', 'nutrient')
  list_filter = ('fertilizer', 'nutrient')


admin.site.register(Fertilizer, FertilizerAdmin)
admin.site.register(NutrientContent, NutrientContentaAdmin)
