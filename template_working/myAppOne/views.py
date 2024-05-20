from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'myAppOne/index.html')

def other(req):
    return render(req,'myAppOne/other.html')

def relative(req):
    return render(req,'myAppOne/relative_url_template.html')