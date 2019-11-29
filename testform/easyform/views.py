from django.shortcuts import render
from . import form
# Create your views here.

def index(request):
    return render(request, 'easyform/index.html')

def form_name(request):
    forms = form.FormExample()

    if request.method == 'POST':
        forms = form.FormExample(request.POST)

        if forms.is_valid():
            print('Validation successs')
            print('NAME:'+forms.cleaned_data['name'])
            print('EMAIL:'+forms.cleaned_data['email'])
            print('TEXT:'+forms.cleaned_data['text'])

    return render(request, 'easyform/example_form.html', {'form':forms})
