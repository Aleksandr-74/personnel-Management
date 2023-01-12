from django.urls import path

from Management_app.views import *

urlpatterns = [
    path('', home),
]