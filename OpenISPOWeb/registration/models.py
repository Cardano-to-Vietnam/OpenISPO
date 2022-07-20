from django.db import models
from django.utils import timezone


from datetime import datetime   
from dateutil.relativedelta import relativedelta


class Disclaimer(models.Model):
    pdf_link = models.CharField(max_length=100)
    version = models.FloatField()
    note = models.CharField(max_length=500)


class ProjectRegistration(models.Model):
    token_name = models.CharField(max_length=100)
    token_num = models.IntegerField()

    start_time = models.DateField(default=timezone.now, blank=False)
    end_time = models.DateField(default =timezone.now, blank=False)

    prefer_pool_num = models.IntegerField()
    prefer_wallet_num = models.IntegerField()

    website = models.URLField(max_length=200)
    email = models.EmailField(verbose_name='Email address', max_length=255)
    phone = models.CharField(max_length=20, null=True)
    
    create_time = models.DateField(default=timezone.now, blank=False)
    disclaimer = models.OneToOneField(Disclaimer, null=True, on_delete=models.SET_NULL)
    
    status_choices = [
        ('registering','registering'),
        ('registered','registered'),
        ('finalized','finalized'),
        ('done','done'),
    ]
    status = models.CharField(max_length=15,choices=status_choices,default='registering')
    note = models.CharField(max_length=200)


class PoolRegistration(models.Model):
    pool_name = models.CharField(max_length=100)
    pool_id = models.CharField(max_length=100)
    prefer_token = models.CharField(max_length=100)
    
    website = models.URLField(max_length=200)
    email = models.EmailField(verbose_name='Email address', max_length=255)
    phone = models.CharField(max_length=20, null=True)
    
    create_time = models.DateField(default=timezone.now, blank=False)
    disclaimer = models.OneToOneField(Disclaimer, null=True, on_delete=models.SET_NULL)

    status_choices = [
        ('registering','registering'),
        ('registered','registered'),
        ('finalized','finalized'),
        ('done','done'),
    ]
    status = models.CharField(max_length=15,choices=status_choices,default='registering')
    note = models.CharField(max_length=200)
