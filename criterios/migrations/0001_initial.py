# Generated by Django 2.2.5 on 2019-10-16 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CriterioNumerico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCriterioN', models.CharField(blank=True, max_length=100)),
                ('numerCriterio', models.IntegerField()),
                ('docCriterio', models.FileField(default='Doc/None/No-doc.pdf', upload_to='Doc/')),
            ],
        ),
    ]
