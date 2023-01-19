from django.urls import path

from Management_app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('employee', FormEmployee, name='worker'),
    path('brigade', FormBrigade, name='brigade'),
    # path("brigade/in>", InfoBrigade, name = 'InfoBrigade')
]