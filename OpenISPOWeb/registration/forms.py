from django import forms
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

from .models import PoolRegistration, ProjectRegistration

from cardano.models import PoolHash

class ProjectRegistrationForm(forms.ModelForm):    
    token_name = forms.CharField(
        label="Token",
        error_messages={'required': ("Token field is required")},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Token name',
            'hx-get': reverse_lazy('registration:validate-proj-subject', kwargs={'subject': 'token_name'},),
            'hx-trigger': 'keyup delay:500ms changed',
            'hx-target': '#div_id_token_name',
        }))
    token_num = forms.CharField(
        label="Number of token",
        error_messages={'required': (
            "Number of token is required"), 'invalid': ("Sai định dạng rồi!!")},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Number of token',
            'hx-get': reverse_lazy('registration:validate-proj-subject', kwargs={'subject': 'token_num'},),
            'hx-trigger': 'keyup delay:500ms changed',
            'hx-target': '#div_id_token_num',
        }))

    start_time = forms.DateField(
        label="From",
        error_messages={'required': ("Start date is required"), 'invalid': (
            "Wrong date format. MM/DD/YY or MM/DD/YYYY")},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'MM/DD/YY or MM/DD/YYYY',
            'hx-get': reverse_lazy('registration:validate-proj-subject', kwargs={'subject': 'start_time'},),
            'hx-trigger': 'keyup delay:500ms changed',
            'hx-target': '#div_id_start_time',
        }))

    end_time = forms.DateField(
        label="To",
        error_messages={'required': ("End date is required"), 'invalid': (
            "Wrong date format. MM/DD/YY or MM/DD/YYYY")},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'MM/DD/YY or MM/DD/YYYY',
            'hx-get': reverse_lazy('registration:validate-proj-subject', kwargs={'subject': 'end_time'},),
            'hx-trigger': 'keyup delay:500ms changed',
            'hx-target': '#div_id_end_time',
        }))

    prefer_pool_num = forms.CharField(
        label="Number of refered pools",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '',
            'hx-get': reverse_lazy('registration:validate-proj-subject', kwargs={'subject': 'prefer_pool_num'},),
            'hx-trigger': 'keyup delay:500ms changed',
            'hx-target': '#div_id_prefer_pool_num',
        }))
    prefer_wallet_num = forms.CharField(
        label="Number of prefered wallets",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '',
            'hx-get': reverse_lazy('registration:validate-proj-subject', kwargs={'subject': 'prefer_wallet_num'},),
            'hx-trigger': 'keyup delay:500ms changed',
            'hx-target': '#div_id_prefer_wallet_num',
        }))

    website = forms.URLField(
        error_messages={'required': ("Website is required"), 'invalid': (
            "Please fill URL format in this field")},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'www.example.com or http(s)://example.com',
            'hx-get': reverse_lazy('registration:validate-proj-subject', kwargs={'subject': 'website'},),
            'hx-trigger': 'keyup delay:500ms changed',
            'hx-target': '#div_id_website',
        }))

    email = forms.EmailField(
        error_messages={'required': ("Email is required"), 'invalid': (
            "Please fill Email format in this field")},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'abc@example.com',
            'hx-get': reverse_lazy('registration:validate-proj-subject', kwargs={'subject': 'email'},),
            'hx-trigger': 'keyup delay:500ms changed',
            'hx-target': '#div_id_email',
        }))

    email2 = forms.EmailField(
        label="Confirm Email",
        error_messages={'required': ("Email is required"), 'invalid': (
            "Please fill Email format in this field")},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the email again',
            'hx-get': reverse_lazy('registration:validate-proj-subject', kwargs={'subject': 'email2'},),
            'hx-trigger': 'keyup delay:500ms changed',
            'hx-target': '#div_id_email2',
        }))

    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '',
            'hx-get': reverse_lazy('registration:validate-proj-subject', kwargs={'subject': 'phone'},),
            'hx-trigger': 'keyup delay:500ms changed',
            'hx-target': '#div_id_phone',
        }))

    disclaimer_agreement = forms.BooleanField(
        label="I have read and agree with the disclaimer",
        required=True)

    captcha = ReCaptchaField(
        required=True,
        label="",
        widget=ReCaptchaV2Checkbox,)

    class Meta:
        model = ProjectRegistration
        fields = ('token_name', 'token_num', 'start_time', 'end_time',
                  'prefer_pool_num', 'prefer_wallet_num', 'website', 'email', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    def clean_token_name(self):
        token_name = self.cleaned_data['token_name']
        if len(token_name) <= 0 or len(token_name) >= 10:
            raise forms.ValidationError(
                "Token name needs to be less than 10 characters")
        else:
            self.fields['token_name'].widget.attrs.update(
                {'class': 'form-control is-valid'})
        return token_name

    def clean_token_num(self):
        token_num = self.cleaned_data['token_num']
        if len(token_num) > 0:
            self.fields['token_num'].widget.attrs.update(
                {'class': 'form-control is-valid'})
        if not token_num.isnumeric():
            raise forms.ValidationError("Please enter a number in this field")
        return token_num

    def clean_start_time(self):
        start_time = self.cleaned_data["start_time"]
        if (start_time):
            self.fields['start_time'].widget.attrs.update(
                {'class': 'form-control is-valid'})
        return start_time

    def clean_end_time(self):
        end_time = self.cleaned_data['end_time']
        if (end_time):
            self.fields['end_time'].widget.attrs.update(
                {'class': 'form-control is-valid'})
        return end_time

    def clean_prefer_pool_num(self):
        prefer_pool_num = self.cleaned_data['prefer_pool_num']
        if len(prefer_pool_num) > 0:
            self.fields['prefer_pool_num'].widget.attrs.update(
                {'class': 'form-control is-valid'})
        if not prefer_pool_num.isnumeric():
            raise forms.ValidationError("Please enter a number in this field")
        return prefer_pool_num

    def clean_prefer_wallet_num(self):
        prefer_wallet_num = self.cleaned_data['prefer_wallet_num']
        if len(prefer_wallet_num) > 0:
            self.fields['prefer_wallet_num'].widget.attrs.update(
                {'class': 'form-control is-valid'})
        if not prefer_wallet_num.isnumeric():
            raise forms.ValidationError("Please enter a number in this field")
        return prefer_wallet_num

    def clean_website(self):
        website = self.cleaned_data['website']
        if (website):
            self.fields['website'].widget.attrs.update({'class': 'form-control is-valid'})
        return website

    def clean_email(self):
        email = self.cleaned_data['email']
        if (email):
            self.fields['email'].widget.attrs.update({'class': 'form-control is-valid'})
        return email

    def clean_email2(self):
        email2 = self.cleaned_data['email2']
        if (email2):
            self.fields['email2'].widget.attrs.update({'class': 'form-control is-valid'})
        return email2

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if (phone):
            self.fields['phone'].widget.attrs.update({'class': 'form-control is-valid'})
        return phone

    def clean(self):
        if 'start_time' in self.cleaned_data and 'end_time' in self.cleaned_data:
            if self.cleaned_data['start_time'] > self.cleaned_data['end_time']:
                self.add_error("end_time", "The end time must be after the start time")
                raise forms.ValidationError("The end time must be after the start time")

        if 'email' in self.cleaned_data and 'email2' in self.cleaned_data:
            if self.cleaned_data['email'] != self.cleaned_data['email2']:
                self.add_error("email2", "Confirmation email is not the same")
                raise forms.ValidationError("Confirmation email is not the same")
        return self.cleaned_data


class PoolRegistrationForm(forms.ModelForm):
    pool_name = forms.CharField(
        error_messages={'required': ("Pool name field is required")},
        widget=forms.TextInput(attrs={
            'class': 'form-control ',
            'hx-get': reverse_lazy('registration:validate-pool-subject', kwargs={'subject': 'pool_name'},),
            'hx-trigger': 'keyup delay:500ms changed',
            'hx-target': '#div_id_pool_name',
        }))

    pool_id = forms.CharField(
        label="Pool ID",
        error_messages={'required': ("Pool ID field is required")},
        widget=forms.TextInput(attrs={
            'hx-get': reverse_lazy('registration:validate-pool-subject', kwargs={'subject': 'pool_id'},),
            'hx-trigger': 'keyup delay:500ms changed',
            'hx-target': '#div_id_pool_id',
        }))

    prefered_tokens = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'AZ, LUNA,...',
            'hx-get': reverse_lazy('registration:validate-pool-subject', kwargs={'subject': 'prefered_tokens'},),
            'hx-trigger': 'keyup delay:500ms changed',
            'hx-target': '#div_id_prefered_tokens',
        }))

    website = forms.URLField(
        error_messages={'required': ("Website is required"), 'invalid': (
            "Please fill URL format in this field")},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'www.example.com or http(s)://example.com',
            'hx-get': reverse_lazy('registration:validate-pool-subject', kwargs={'subject': 'website'},),
            'hx-trigger': 'keyup delay:500ms changed',
            'hx-target': '#div_id_website',
        }))

    email = forms.EmailField(
        error_messages={'required': ("Email is required"), 'invalid': (
            "Please fill Email format in this field")},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'abc@example.com',
            'hx-get': reverse_lazy('registration:validate-pool-subject', kwargs={'subject': 'email'},),
            'hx-trigger': 'keyup delay:500ms changed',
            'hx-target': '#div_id_email',
        }))

    email2 = forms.EmailField(
        label="Confirm Email",
        error_messages={'required': ("Email is required"), 'invalid': (
            "Please fill Email format in this field")},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the email again',
            'hx-get': reverse_lazy('registration:validate-pool-subject', kwargs={'subject': 'email2'},),
            'hx-trigger': 'keyup delay:500ms changed',
            'hx-target': '#div_id_email2',
        }))

    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '',
            'hx-get': reverse_lazy('registration:validate-pool-subject', kwargs={'subject': 'phone'},),
            'hx-trigger': 'keyup delay:500ms changed',
            'hx-target': '#div_id_phone',
        }))

    disclaimer_agreement = forms.BooleanField(
        label="I have read and agree with the disclaimer",
        required=True
    )

    captcha = ReCaptchaField(
        required=True,
        label="",
        widget=ReCaptchaV2Checkbox,)


    class Meta:
        model = PoolRegistration
        fields = ('pool_name', 'pool_id', 'prefered_tokens', 'website', 'email', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    def clean_pool_name(self):
        pool_name = self.cleaned_data['pool_name']
        if len(pool_name) <= 0 or len(pool_name) >= 30:
            raise forms.ValidationError(
                "Pool name needs to be less than 30 characters")
        else:
            self.fields['pool_name'].widget.attrs.update(
                {'class': 'form-control is-valid'})
        return pool_name

    def clean_pool_id(self):
        pool_id = self.cleaned_data['pool_id']
        if (pool_id):
            self.fields['pool_id'].widget.attrs.update(
                {'class': 'form-control is-valid'})
        return pool_id

    def clean_prefered_tokens(self):
        prefered_tokens = self.cleaned_data['prefered_tokens']
        if (prefered_tokens):
            self.fields['prefered_tokens'].widget.attrs.update({'class': 'form-control is-valid'})
        return prefered_tokens

    def clean_website(self):
        website = self.cleaned_data['website']
        if (website):
            self.fields['website'].widget.attrs.update({'class': 'form-control is-valid'})
        return website

    def clean_email(self):
        email = self.cleaned_data['email']
        if (email):
            self.fields['email'].widget.attrs.update({'class': 'form-control is-valid'})
        return email

    def clean_email2(self):
        email2 = self.cleaned_data['email2']
        if (email2):
            self.fields['email2'].widget.attrs.update({'class': 'form-control is-valid'})
        return email2

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if (phone):
            self.fields['phone'].widget.attrs.update({'class': 'form-control is-valid'})
        return phone

    def clean(self):
        if 'captcha' not in self.cleaned_data:
            self.add_error("captcha", "Captcha is required")

        if 'email' in self.cleaned_data and 'email2' in self.cleaned_data:
            if self.cleaned_data['email'] != self.cleaned_data['email2']:
                self.add_error("email2", "Confirmation email is not the same")
            if not PoolHash.objects.using('cardano').filter(view=self.cleaned_data['pool_id']).exists():
                self.add_error("pool_id", "This Pool ID is not exists")
        return self.cleaned_data
