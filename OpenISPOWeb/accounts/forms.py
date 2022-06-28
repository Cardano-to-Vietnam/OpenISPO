from django.contrib.auth.forms import UserCreationForm

from .models import ProjectUser
from django import forms

class ProjectUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    address = forms.CharField(required=True)

    class Meta:
        model = ProjectUser
        fields = ("email", "name", "phone", "address", "password1", "password2")

    def save(self, commit=True):
        user = super(ProjectUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user