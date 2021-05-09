from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        'users' : User.objects.all()
        }
    
    return render(request, 'index.html', context)

def add_user(request):
  if request.method == "POST":
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    age = request.POST['age']
    email_address = request.POST['email_address']
    User.objects.create(
        first_name=first_name, 
        last_name=last_name, 
        age = age,
        email_address=email_address
        )
    
  return redirect('/')
def result (request, id):
  if request.method == "POST":
    print(request.POST)
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    age = request.POST['age']
    email_address = request.POST['email_address']
    user = User.objects.get(id=id)
    user.first_name = first_name
    user.last_name = last_name
    user.email_address = email_address
    user.age = age
    user.save()
    return redirect('/')
  user_edit = User.objects.get(id=id)
  context = {
      "user" : user_edit
  }
  return render(request, 'result.html', context)
def reset(request, id):
  User.objects.get(id=id).delete()
  return redirect("/")