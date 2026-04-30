from django.urls import path
from .views import RegistroView, LoginView, LoginAPIView, RegistroAPIView

urlpatterns = [
    path('',              RegistroView.as_view(),    name='registro'),
    path('login/',        LoginView.as_view(),        name='login'),
    path('api/login/',    LoginAPIView.as_view(),     name='api_login'),
    path('api/registro/', RegistroAPIView.as_view(),  name='api_registro'),
]