from tkinter.ttk import LabeledScale
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import PoolRegistration, ProjectRegistration

class PoolRegistrationForm(forms.ModelForm):
    pool_name = forms.CharField()
    pool_id = forms.CharField()
    prefered_tokens = forms.CharField()
    website = forms.URLField()
    email = forms.EmailField()
    phone = forms.CharField()
    disclaimer_agreement = forms.BooleanField(label="I have readd and agree with the disclaimer", required=True)

    class Meta:
        model=PoolRegistration
        fields=('pool_name', 'pool_id', 'prefered_tokens', 'website')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('pool_name', css_class='form-group col-md-6 mb-0'),
                Column('pool_id', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'website',
            'prefered_tokens',
            Row(
                Column('email', css_class='form-group col-md-8 mb-0'),
                Column('phone', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'disclaimer_agreement',
            Submit('submit', 'Register')
        )

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