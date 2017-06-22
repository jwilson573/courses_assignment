from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^addCourse$', views.addCourse),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^confirm/(?P<id>\d+)$', views.confirm)
]
