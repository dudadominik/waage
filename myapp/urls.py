from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^cool', views.post_list, name='post_list'),
]
