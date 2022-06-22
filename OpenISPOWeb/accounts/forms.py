from django.contrib.auth.forms import UserCreationForm

from .models import ProjectUser
from django import forms



class ProjectUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = ProjectUser
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super(ProjectUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user