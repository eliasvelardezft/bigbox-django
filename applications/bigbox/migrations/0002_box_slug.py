# Generated by Django 2.2 on 2021-08-06 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='slug',
            field=models.CharField(max_length=20, null=True),
        ),
    ]