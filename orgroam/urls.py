from django.urls import path

from . import views

urlpatterns = [
    path('', views.orgroam, name='orgroam'),
    path('nodes', views.nodes, name='nodes'),
    path('nodes/<str:id>', views.node, name='node'),
    path('read/<str:id>', views.read, name='read'),
    path('links', views.links, name='links'),
    path('tags', views.tags, name='tags'),
]
