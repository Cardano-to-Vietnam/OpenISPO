from re import A
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.contrib.sites.shortcuts import get_current_site  
from django.core.mail import EmailMessage  

from django.template.loader import render_to_string  

from crispy_forms.templatetags.crispy_forms_filters import as_crispy_field

from .forms import PoolRegistrationForm, ProjectRegistrationForm
from .tokens import email_verification_token  
from .models import ProjectRegistration
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
            project=form.save(commit=False)
            project.status = 'registering'
            form.save()

            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email'  
            message = render_to_string('registration/emailverify.html', {  
                'project': project,  
                'domain': current_site.domain,  
                'prjid':urlsafe_base64_encode(force_bytes(project.pk)),  
                'token':email_verification_token.make_token(project),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(mail_subject, message, to=[to_email])  
            email.send()  

            messages.success(request, "Registration successful.")
            return redirect("registration:regis_done")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            return render (request=request, template_name="registration/projectregistration.html", context={"projectregis_form":form})

    form = ProjectRegistrationForm()
    return render (request=request, template_name="registration/projectregistration.html", context={"projectregis_form":form})

def validate_proj_subject(request, subject):
    form = ProjectRegistrationForm(request.GET)
    return HttpResponse(as_crispy_field(form[subject]))

def register_done_view(request):
    return HttpResponse("Please confirm your email address to complete the registration")

def project_email_verify(request, prjidb64, token):  
    ProjectModel = ProjectRegistration  
    try:  
        prjid = force_str(urlsafe_base64_decode(prjidb64))
        print("prjid",prjid)
        project = ProjectModel.objects.get(pk=prjid)  
    except(TypeError, ValueError, OverflowError, ProjectModel.DoesNotExist):  
        project = None  
    if project is not None and email_verification_token.check_token(project, token):  
        project.status = "registered"  
        project.save()  
        return HttpResponse('Thank you for your email confirmation.')  
    else:  
        return HttpResponse('Activation link is invalid!')