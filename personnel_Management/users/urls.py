from django.urls import path, include

from users.views import Register, LoginUsers

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginUsers.as_view(), name='login')

]
