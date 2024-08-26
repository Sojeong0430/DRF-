from django.urls import path , include
from . import views

#127.0.0.1:8000/todo/

urlpatterns = [
    path("create/",views.TodoCreateAPI.as_view(),name='create'),
    path("list/",views.TodoListAPI.as_view(),name='list'),
    path("retrive/<int:pk>",views.TodoRetrive.as_view(),name='retrive'),
    path("update/<int:pk>",views.TodoUpdateAPI.as_view(),name='patch'),
    path("delete/<int:pk>",views.TodoDeleteAPI.as_view())
]
