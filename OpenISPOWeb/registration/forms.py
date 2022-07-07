from cProfile import label
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

from .models import PoolRegistration, ProjectRegistration

class PoolRegistrationForm(forms.ModelForm):
    pool_name = forms.CharField(
        error_messages={'required': ("Pool name field is required")},
        widget=forms.TextInput(attrs={
                'class': 'form-control is-valid',
                'hx-get': reverse_lazy('registration:validate-pool-subject', kwargs={'subject': 'pool_name'},),
                'hx-trigger': 'keyup changed',
                'hx-target': '#div_id_pool_name',
                }))

    pool_id = forms.CharField(
        error_messages={'required': ("Pool ID field is required")},
        widget=forms.TextInput(attrs={
                'hx-get': reverse_lazy('registration:validate-pool-subject', kwargs={'subject': 'pool_id'},),
                'hx-trigger': 'keyup',
                'hx-target': '#div_id_pool_id',
                }))

    prefered_tokens = forms.CharField()

    website = forms.URLField()

    email = forms.EmailField(
        error_messages={'required': ("Cần phải nhập email"), 'invalid': ("Sai format email rồi!!")}, 
        widget=forms.EmailInput(attrs={
                'hx-get': reverse_lazy('registration:validate-pool-subject', kwargs={'subject': 'email'},),
                'hx-target': '#div_id_email',
                }))

    phone = forms.CharField(widget=forms.TextInput(attrs={
                'hx-get': reverse_lazy('registration:validate-pool-subject', kwargs={'subject': 'email'},),
                'hx-target': '#div_id_email',
                }))

    disclaimer_agreement = forms.BooleanField(
        label="I have readd and agree with the disclaimer", 
        required=True
        )

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)


    class Meta:
        model=PoolRegistration
        fields=('pool_name', 'pool_id', 'prefered_tokens', 'website')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {"novalidate": 'novalidate'}
        self.fields['pool_name'].widget.attrs.update({'autofocus': True})


    def clean_pool_name(self):
        pool_name = self.cleaned_data['pool_name']
        if len(pool_name) < 3:
            raise forms.ValidationError("Too shorrt!!!!")
        return pool_name
    
    def clean_pool_id(self):
        pool_id = self.cleaned_data['pool_id']
        if len(str(pool_id)) < 3:
            raise forms.ValidationError("pool id Too shorrt!!!!")
        return pool_id

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("This email already exists")
        return email
        

class ProjectRegistrationForm(forms.ModelForm):
    token_name = forms.CharField(
        label="Token",
        error_messages={'required': ("Token field is required")},
        widget=forms.TextInput(attrs={
                'class': 'form-control is-valid',
                'placeholder': 'Token name',
                'hx-get': reverse_lazy('registration:validate-proj-subject', kwargs={'subject': 'token_name'},),
                'hx-trigger': 'keyup changed',
                'hx-target': '#div_id_token_name',
                # 'required': '',
                }))
    token_num = forms.CharField(
        label="Number of token",
        error_messages={'required': ("Number of token is required"), 'invalid': ("Sai định dạng rồi!!")},
        widget=forms.TextInput(attrs={
                'class': 'form-control is-valid',
                'placeholder': 'Number of token',
                'hx-get': reverse_lazy('registration:validate-proj-subject', kwargs={'subject': 'token_num'},),
                'hx-trigger': 'keyup changed',
                'hx-target': '#div_id_token_num',
                }))
    
    start_time = forms.DateTimeField(
        label="From",
        error_messages={'required': ("Start date is required"), 'invalid': ("Wrong date format. MM/DD/YY or MM/DD/YYYY")},
        widget=forms.TextInput(attrs={
                'class': 'form-control is-valid',
                'placeholder': 'MM/DD/YY or MM/DD/YYYY',
                'hx-get': reverse_lazy('registration:validate-proj-subject', kwargs={'subject': 'start_time'},),
                'hx-trigger': 'keyup changed',
                'hx-target': '#div_id_start_time',
                }))

    end_time = forms.DateTimeField(label="To")

    prefer_pool_num = forms.CharField(label="Number of refered pools")
    prefer_wallet_num = forms.CharField(label="Number of prefered wallets")

    website = forms.URLField()
    email = forms.EmailField()
    email2 = forms.EmailField(
        label="Confirm Email"
    )
    phone = forms.CharField()
    disclaimer_agreement = forms.BooleanField(
        label="I have read and agree with the disclaimer", 
        required=True)

    captcha = ReCaptchaField(
        label="",
        widget=ReCaptchaV2Checkbox,)

    class Meta:
        model=ProjectRegistration
        fields=('token_name', 'token_num', 'start_time', 'end_time', 'prefer_pool_num', 'prefer_wallet_num', 'website', 'email','phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    def clean_token_name(self):
        token_name = self.cleaned_data['token_name']
        if len(token_name) >= 10:
            raise forms.ValidationError("Token name needs to be less than 10 characters")
        return token_name

    def clean_token_num(self):
        token_num = self.cleaned_data['token_num']
        print(token_num.isnumeric())
        if not token_num.isnumeric():
            raise forms.ValidationError("Please enter a number in this field")
        return token_num