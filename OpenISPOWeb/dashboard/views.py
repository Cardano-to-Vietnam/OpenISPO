from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your models here.
def project_dashboard(request):
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    if request.user.user_type =="token_distributor":
        return render(request,template_name= "project.html", context={"infor":"dashboard"})
    return render(request,template_name= "project.html", context={"infor":"dashboard"})

def project_contract(request):
    return render(request,template_name= "project.html", context={"infor":"contract"})
def project_notification(request):
    return render(request,template_name= "project.html", context={"infor":"notification"})
def delegator_dashboard(request):
    return render(request,template_name= "delegator_dashboard.html")
def pool_dashboard(request):
    return render(request, template_name="pool.html",context={"infor":"dashboard"})
def pool_contract(request):
    return render(request, template_name="pool.html",context={"infor":"contract"})
def pool_notification(request):
    return render(request, template_name="pool.html", context={"infor":"notification"})
def admin(request):
    pass