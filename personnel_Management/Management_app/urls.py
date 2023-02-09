from django.urls import path

from Management_app.views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('workers', AddWorker.as_view(), name='workers'),
    path('brigades', AddBrigade.as_view(), name='brigades'),
    path('request', AddObject.as_view(), name='request'),
    path('workers/<int:worker_id>/', DetailWorker.as_view(), name='worker'),
    path('brigades/<int:brigade_id>/', DatailBrigade.as_view(), name='brigade'),
    path('ojectes/<int:objectes_id>/', DataiObjects.as_view(), name='objecte'),
    path('brigades/<int:brigade_id>/api/v1/brigadesAPI/<int:pk>', BrigadeAPI.as_view()),
    path('workers/<int:worker_id>/api/v1/workersAPI/<int:pk>', WorkerAPI.as_view()),
    # path('request/api/v1/objectAPI/', AddObjectAPI.as_view(), name='create'),
]