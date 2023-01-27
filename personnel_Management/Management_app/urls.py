from django.urls import path

from Management_app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('workers', WorkerFormView, name='workers'),
    path('brigades', BrigadeFormView, name='brigades'),
    path('workers/<int:worker_id>/', InfoWorker, name='worker'),
    path('brigades/<int:brigade_id>/', InfoBrigade, name='brigade'),
    path('request', FormObject, name='request'),
    path('api/v1/brigadesAPI', BrigadesAPIList.as_view()),
    path('api/v1/brigadesAPI/<int:pk>', BrigadesAPIList.as_view())
]