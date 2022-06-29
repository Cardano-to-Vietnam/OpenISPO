# Generated by Django 3.2.6 on 2022-06-28 08:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disclaimer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_link', models.CharField(max_length=100)),
                ('version', models.FloatField()),
                ('note', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_name', models.CharField(max_length=100)),
                ('token_num', models.IntegerField()),
                ('start_time', models.DateTimeField(default=datetime.datetime(2022, 6, 28, 15, 0, 36, 189772))),
                ('end_time', models.DateTimeField(default=datetime.datetime(2022, 6, 28, 15, 0, 36, 189772))),
                ('prefer_pool_num', models.IntegerField()),
                ('prefer_wallet_num', models.IntegerField()),
                ('website', models.URLField()),
                ('status', models.CharField(choices=[('registered', 'registered'), ('finalized', 'finalized'), ('done', 'done')], default='registered', max_length=15)),
                ('note', models.CharField(max_length=200)),
                ('disclaimer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.disclaimer')),
            ],
        ),
        migrations.CreateModel(
            name='PoolRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pool_name', models.CharField(max_length=100)),
                ('pool_id', models.IntegerField()),
                ('prefer_token', models.CharField(max_length=100)),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('status', models.CharField(choices=[('registered', 'registered'), ('finalized', 'finalized'), ('done', 'done')], default='registered', max_length=15)),
                ('note', models.CharField(max_length=200)),
                ('disclaimer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.disclaimer')),
            ],
        ),
    ]