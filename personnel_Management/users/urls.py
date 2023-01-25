from django.urls import path, include

from users.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('regisner/', Register.as_view(), name='register')

]
