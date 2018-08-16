from django.conf.urls import url

from fertilizers.views import FertilizersListView


urlpatterns = [
  url('^$', FertilizersListView.as_view(), name='fertilizers-list'),
]
