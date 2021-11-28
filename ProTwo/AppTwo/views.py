from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.
def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'AppTwo/help.html',context=helpdict)

def index(request):
    return render(request,'AppTwo/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {"users":user_list}
    return render(request,'AppTwo/users.html',context=user_dict)
