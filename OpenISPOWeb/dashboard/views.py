from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your models here.
def project(request):
    return render(request,template_name= "project.html")
def delegator(request):
    return render(request,template_name= "delegator.html")
def pool(request):
    return render(request, template_name="pool.html")
def admin(request):
    pass