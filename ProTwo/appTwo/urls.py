from django.urls import path
from appTwo import views
urlpatterns = [
    path("help/",views.help),
    path("count/",views.countNumber),
]