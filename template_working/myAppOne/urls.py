from django.urls import path
from myAppOne import views

#TEMPLATE TAGGING 
app_name = 'myAppOne'
urlpatterns = [
    path("relative/",views.relative,name='relative'),
    path("other/",views.other,name='other')
]