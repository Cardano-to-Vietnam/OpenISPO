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
                'hx-get': reverse_lazy('registration:validate-subject', kwargs={'subject': 'pool_name'},),
                'hx-trigger': 'keyup changed',
                'hx-target': '#div_id_pool_name',
                }))

    pool_id = forms.CharField(
        error_messages={'required': ("Pool ID field is required")},
        widget=forms.TextInput(attrs={
                'hx-get': reverse_lazy('registration:validate-subject', kwargs={'subject': 'pool_id'},),
                'hx-trigger': 'keyup',
                'hx-target': '#div_id_pool_id',
                }))

    prefered_tokens = forms.CharField()

    website = forms.URLField()

    email = forms.EmailField(
        error_messages={'required': ("Cần phải nhập email"), 'invalid': ("Sai format email rồi!!")}, 
        widget=forms.EmailInput(attrs={
                'hx-get': reverse_lazy('registration:validate-subject', kwargs={'subject': 'email'},),
                'hx-target': '#div_id_email',
                }))

    phone = forms.CharField(widget=forms.TextInput(attrs={
                'hx-get': reverse_lazy('registration:validate-subject', kwargs={'subject': 'email'},),
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
    token_name = forms.CharField(label="Token")
    token_num = forms.CharField(label="Number of token")
    
    start_time = forms.DateTimeField(label="From")
    end_time = forms.DateTimeField(label="To")

    prefer_pool_num = forms.CharField(label="Number of refered pools")
    prefer_wallet_num = forms.CharField(label="Number of prefered wallets")

    website = forms.URLField()
    email = forms.EmailField()
    phone = forms.CharField()
    disclaimer_agreement = forms.BooleanField(label="I have readd and agree with the disclaimer", required=True)

    class Meta:
        model=ProjectRegistration
        fields=('token_name', 'token_num', 'start_time', 'end_time', 'prefer_pool_num', 'prefer_wallet_num', 'website', 'email','phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('token_name', css_class='form-group col-md-8 mb-0'),
                Column('token_num', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('start_time', css_class='form-group col-md-6 mb-0'),
                Column('end_time', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('prefer_pool_num', css_class='form-group col-md-6 mb-0'),
                Column('prefer_wallet_num', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'website',
            Row(
                Column('email', css_class='form-group col-md-8 mb-0'),
                Column('phone', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'disclaimer_agreement',
            Submit('submit', 'Register')
        )