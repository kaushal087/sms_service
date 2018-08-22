from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.Login.as_view(), name='user_login'),
    path('signup/', views.SignUp.as_view(), name='user_signup'),
]
