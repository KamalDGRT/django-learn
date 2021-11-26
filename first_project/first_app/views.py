from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dictionary = {
        'insert_content': 'Now, rendering from first_app/index.html!'
    }
    return render(
        request,
        'first_app/index.html',
        context=my_dictionary
    )
