# Generated by Django 4.1.1 on 2022-10-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_alter_application_attached_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application_count',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
