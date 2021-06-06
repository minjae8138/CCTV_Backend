from django.conf.urls.static import static
from django.urls import path

from backend import settings
from . import views

urlpatterns = [
    path('makeId', views.makeId),
    path('infoDetail', views.infoGet)
]
