# Generated by Django 4.2.4 on 2023-08-11 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='name',
        ),
        migrations.AddField(
            model_name='home',
            name='mainpara',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='paragraph',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='pricing',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='servicesimg',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='home',
            name='servicespara',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
