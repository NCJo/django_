from django.conf.urls import url
from rango import views, view_about

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', view_about.about, name='about'),
]