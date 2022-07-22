from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import ProjectUser
from django import forms

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
        user = super(ProjectUserCreationForm, self).save(commit=False)
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
        