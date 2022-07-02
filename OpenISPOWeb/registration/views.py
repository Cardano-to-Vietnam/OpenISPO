from re import A
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse


from crispy_forms.templatetags.crispy_forms_filters import as_crispy_field


from .forms import PoolRegistrationForm, ProjectRegistrationForm
from accounts.models import ProjectUser


def pool_register_request_view(request):
    if request.method == "POST":
        form = PoolRegistrationForm(request.POST)
        if form.is_valid():
            user = ProjectUser(email=form.cleaned_data['email'],phone=form.cleaned_data['phone'])
            user.save()
            form.save()
            messages.success(request, "Registration successful." )
            return redirect("registration:regis_done")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = PoolRegistrationForm()
    return render (request=request, template_name="registration/poolregistration.html", context={"poolregis_form":form})

def validate_pool_subject(request, subject):
    form = PoolRegistrationForm(request.GET)
    return HttpResponse(as_crispy_field(form[subject]))

def project_register_request_view(request):
    if request.method == "POST":
        form = ProjectRegistrationForm(request.POST)
        if form.is_valid():
            user = ProjectUser(email=form.cleaned_data['email'],phone=form.cleaned_data['phone'])
            user.save()
            form.save()
            messages.success(request, "Registration successful." )
            return redirect("registration:regis_done")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            print("DEBUG", "Unsuccessful registration. Invalid information.",form)
    form = ProjectRegistrationForm()
    return render (request=request, template_name="registration/projectregistration.html", context={"projectregis_form":form})


def register_done_view(request):
    return HttpResponse("Your resgister is in processing")