# Generated by Django 3.2.5 on 2022-10-24 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('telephone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Street Address')),
                ('complex_building', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complex/Building')),
                ('suburb', models.CharField(blank=True, max_length=100, null=True, verbose_name='Suburb')),
                ('town', models.CharField(blank=True, max_length=100, null=True, verbose_name='Town/City')),
                ('province', models.CharField(blank=True, max_length=100, null=True, verbose_name='Province')),
                ('post_code', models.CharField(blank=True, max_length=8, null=True, verbose_name='Post Code')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Country')),
                ('longitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Longitude')),
                ('latitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Latitude')),
                ('captcha_score', models.FloatField(default=0.0)),
                ('has_profile', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]