from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test/$', views.line_chart, name='line_chart'),
    url(r'^a/$', views.confirm_ajax, name='confirm_ajax'),
]
