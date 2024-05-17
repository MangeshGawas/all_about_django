from django.shortcuts import render
from . import forms

# Create your views here.
def index(req):
    return render(req, 'basicapp/index.html')

def form_name_view(req):
    form = forms.FormName()
    form_data = {"name": "", "email": "", "text": ""}
    
    if req.method == 'POST':
        form = forms.FormName(req.POST)
        if form.is_valid():
            print('Validation successful')
            print("Name:", form.cleaned_data['name'])
            print("Email:", form.cleaned_data['email'])
            print("Text:", form.cleaned_data['text'])
            form_data = {
                "name": form.cleaned_data['name'],
                "email": form.cleaned_data['email'],
                "text": form.cleaned_data['text']
            }

    context = {
        'form': form,
        'form_data': form_data
    }
    
    return render(req, 'basicapp/form_page.html', context)
