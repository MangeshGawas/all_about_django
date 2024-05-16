from django.shortcuts import render
from appThree.models import User

# Create your views here.
def index(req):
    return render(req,'appThree/index.html')

def user(req):
    user_list = User.objects.order_by('first_name')
    user_dict = {'user':user_list}
    return render(req, 'appThree/user.html',context=user_list)