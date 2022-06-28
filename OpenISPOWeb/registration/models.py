from django.db import models
from django.utils import timezone


from datetime import datetime   
from dateutil.relativedelta import relativedelta


class Disclaimer(models.Model):
    pdf_link = models.CharField(max_length=100)
    version = models.FloatField()
    note = models.CharField(max_length=500)

class PoolRegistration(models.Model):
    pool_name = models.CharField(max_length=100)
    pool_id = models.IntegerField()
    prefer_token = models.CharField(max_length=100)

    website = models.URLField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    disclaimer = models.OneToOneField(Disclaimer, null=True, on_delete=models.SET_NULL)

    status_choices = [
        ('registered','registered'),
        ('finalized','finalized'),
        ('done','done'),
    ]
    status = models.CharField(max_length=15,choices=status_choices,default='registered')
    note = models.CharField(max_length=200)


class ProjectRegistration(models.Model):
    token_name = models.CharField(max_length=100)
    token_num = models.IntegerField()

    start_time = models.DateTimeField(default=datetime.now(), blank=False)
    end_time = models.DateTimeField(default = datetime.now() + relativedelta(month=6), blank=False)

    prefer_pool_num = models.IntegerField()
    prefer_wallet_num = models.IntegerField()

    website = models.URLField(max_length=200)

    disclaimer = models.OneToOneField(Disclaimer, null=True, on_delete=models.SET_NULL)

    status_choices = [
        ('registered','registered'),
        ('finalized','finalized'),
        ('done','done'),
    ]
    status = models.CharField(max_length=15,choices=status_choices,default='registered')
    note = models.CharField(max_length=200)