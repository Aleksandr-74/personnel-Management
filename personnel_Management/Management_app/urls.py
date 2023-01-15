from django.urls import path

from Management_app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('employee', FormEmployee, name='employee'),
    path('brigade', FormBrigade, name='brigade')
]