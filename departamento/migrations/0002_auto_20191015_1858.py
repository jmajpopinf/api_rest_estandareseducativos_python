# Generated by Django 2.2.5 on 2019-10-16 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='nombreDepartamento',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='distrito',
            name='nombreDistrito',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]