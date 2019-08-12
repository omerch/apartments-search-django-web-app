from django.conf.urls import url
from .views import ListingsRudView, ListingsAPIView

urlpatterns = [
    url(r'^$', ListingsAPIView.as_view(), name='post-create'),
    url(r'^(?P<pk>\d+)/$', ListingsRudView.as_view(), name='post-rud'),
]