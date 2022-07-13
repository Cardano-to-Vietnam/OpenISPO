from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from .forms import ProjectUserCreationForm

def login_done(request):
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    return render(request=request, template_name="accounts/logindone.html")

def login_request(request):
    if request.user.is_authenticated:
        return render(request=request, template_name="accounts/logindone.html")

    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("accounts:logindone")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    return render(request=request, template_name="accounts/login.html", context={"login_form":form})

def register_request(request):
    if request.method == "POST":
        form = ProjectUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("accounts:logindone")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    return render (request=request, template_name="accounts/register.html", context={"register_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("accounts:login")