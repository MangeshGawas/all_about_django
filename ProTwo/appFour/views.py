from django.shortcuts import render
# from django.http import HttpResponse
from appFour.form import NewUserForm

# Create your views here.
def index(req):
    return render(req,'appFour/index.html')

def user(req):
    form = NewUserForm()
    if req.method =='POST':
        form = NewUserForm(req.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(req)
        else:
            print("Form is invalid ")

    return render(req,'appFour/usermodelsave.html',{'form':form})
