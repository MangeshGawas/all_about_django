from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Hello World")

def index(request):
    my_dict = {'name':"Mangesh"}
    return render(request,'index.html',context=my_dict)