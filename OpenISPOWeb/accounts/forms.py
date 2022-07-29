from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import ProjectUser
from django import forms

from django.core.mail import EmailMessage  
from django.template.loader import render_to_string 
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class ProjectUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    status_choices = [
        ('activate','Activate'),
        ('lock','Lock'),
    ]
    status = forms.ChoiceField(
        choices=status_choices,
        widget=forms.RadioSelect(),
        initial="activate")
    
    user_type_choices = [
        ('token_distributor','Token distributor'),
        ('pools_owner','Pools owner'),
    ]
    user_type = forms.ChoiceField(
        choices=user_type_choices, 
        widget=forms.RadioSelect(),
        initial="token_distributor")

    random_password_button = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            'value': 'Random Password',
            'type': 'button',
            'onClick': 'random_password()'
        }))

    class Meta:
        model = ProjectUser
        fields = ("email", "status", "user_type")

    def save(self, commit=True):
        user = super().save(commit=False)
        user_email = self.cleaned_data["email"]
        user_password = self.cleaned_data["password1"]
        user.set_password(user_password)
        
        # Send activate notify to user email
        mail_subject = '[OPENISPO] Your acount is activated'  
        message = render_to_string('accounts/accountcreateemailnotify.html', {  
            "email": user_email,
            "password": user_password,
        })  
        to_email = user_email 
        email = EmailMessage(mail_subject, message, to=[to_email])  
        email.send() 

        if commit:
            user.save()
        return user

class ProjectUserChangeForm(UserChangeForm):
    status_choices = [
        ('activate','Activate'),
        ('lock','Lock'),
    ]
    status = forms.ChoiceField(
        choices=status_choices,
        widget=forms.RadioSelect(),
        initial="activate")
    
    user_type_choices = [
        ('token_distributor','Token distributor'),
        ('pools_owner','Pools owner'),
    ]
    user_type = forms.ChoiceField(
        choices=user_type_choices, 
        widget=forms.RadioSelect(),
        initial="token_distributor")

    class Meta:
        model = ProjectUser
        fields = ("email", "status", "user_type",)
        
class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control"}))
    password = forms.CharField(
        label= ("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": "form-control"}),
    )