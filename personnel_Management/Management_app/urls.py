from django.urls import path

from Management_app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('workers', FormWorker, name='workers'),
    path('brigades', FormBrigade, name='brigades'),
    path('workers/<int:worker_id>/', InfoWorker, name='worker'),
    path('brigades/<int:brigade_id>/', InfoBrigade, name='brigade'),
    path('request', FormObject, name='request')
]