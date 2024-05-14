from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return(HttpResponse("<em>MY second Project</em>"))

my_dic = {"Help":"How Can I help You"}
def help(req):
    return render(req,'index.html',context=my_dic)

def countNumber(request):
    numbers = ""
    for i in range(10):
        numbers +=f"{i},"
    return HttpResponse(numbers)

    