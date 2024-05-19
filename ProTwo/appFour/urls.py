from django.urls import path
from appFour import views
urlpatterns = [
    path("",views.index),
    path("user/",views.user),
]