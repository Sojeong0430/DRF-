from django.urls import path
from .views import UserRegisterView,UserlistView,LoginAPI,LogoutAPI

#127.0.0.1:8000/accounts/

urlpatterns = [
    path('register/',UserRegisterView.as_view()),
    path('userlist/',UserlistView.as_view()),
    path('login/',LoginAPI.as_view()),
    path('logout/',LogoutAPI.as_view())
]
