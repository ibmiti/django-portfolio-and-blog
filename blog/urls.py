from django.urls import path
from . import views


# list of urls
urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
]
