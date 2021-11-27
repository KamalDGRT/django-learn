from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    message = {
        'help_me': 'Help me from views.py of ProTwo!'
    }
    return render(
        request,
        'ProTwo/index.html',
        context=message
    )
