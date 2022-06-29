from django.contrib.auth.forms import UserCreationForm

from .models import ProjectUser
from django import forms

class ProjectUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)

    class Meta:
        model = ProjectUser
        fields = ("email", "phone")

    def save(self, commit=True):
        user = super(ProjectUserCreationForm, self).save(commit=False)
        raw_password = ProjectUser.objects.make_random_password()
        user.set_password(raw_password)
        if commit:
            user.save()
        return user