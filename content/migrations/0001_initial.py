# Generated by Django 3.2.9 on 2021-11-23 06:36

import content.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_auto_20211123_1206'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application_Count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_cnt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('abbreviation', models.CharField(default='', max_length=10)),
                ('receiver_authority_id', models.IntegerField(default=1)),
                ('requirements_info', models.TextField(default='Requirement information needs to be updated.')),
                ('max_step', models.IntegerField(default='1')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.department', verbose_name='Department')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('app_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('category', models.CharField(default='', max_length=300)),
                ('title', models.CharField(default='', max_length=300)),
                ('attached_pdf', models.FileField(blank=True, default=None, null=True, upload_to='documents/')),
                ('current_authority', models.IntegerField(default='', max_length=300)),
                ('current_step', models.IntegerField(default='0')),
                ('max_step', models.IntegerField(default='1')),
                ('is_approved', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('applicant', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Applicant')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.department', verbose_name='Department')),
                ('request', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='content.scholarship', verbose_name='Request')),
            ],
        ),
    ]