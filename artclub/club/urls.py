from django.conf.urls import url
from . import views

app_name = 'club'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^team/', views.team, name='team'),
    url(r'^events/', views.events, name='events'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^gallery/', views.gallery, name='gallery'),


]