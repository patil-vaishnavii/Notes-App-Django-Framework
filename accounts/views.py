from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

def register(request):

  if request.method == "POST":

    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]

    user = User.objects.create_user(
      username=username,
      email=email,
      password=password
    )

    login(request,user)

    return redirect("home")

  return render(request,"accounts/register.html")

def login_view(request):
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(
      request,
      username=username,
      password=password
    )

    if user is not None:
      login(request,user)
      return redirect("home")

  return render(request,"accounts/login.html")

def logout_view(request):
  logout(request)
  return redirect("login")