from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,WebPage,AccessRecord
# Create your views here.

# def index(request):
#     return HttpResponse("Hello World")

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    my_dict = {'name':"Mangesh"}
    return render(request,'index.html',context=date_dict)