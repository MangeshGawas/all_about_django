from django.urls import path
from appThree import views
urlpatterns = [
    path("",views.index),
    path("user/",views.user),
]