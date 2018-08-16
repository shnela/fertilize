from django.views.generic import ListView

from fertilizers.models import Fertilizer


class FertilizersListView(ListView):
  template_name = 'fertilizers/fertilizers_list.html'
  model = Fertilizer
  context_object_name = 'fertilizers_list'
