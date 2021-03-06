# Generated by Django 2.2 on 2021-08-05 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('internal_name', models.CharField(max_length=200)),
                ('description', models.TextField(verbose_name='descripción')),
                ('purchase_available', models.BooleanField(default=False, verbose_name='disponible venta individual')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nombre')),
                ('slug', models.SlugField()),
                ('order', models.IntegerField(default=0, verbose_name='orden')),
                ('description', models.TextField(verbose_name='descripción')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nombre')),
                ('slug', models.SlugField()),
                ('order', models.IntegerField(default=0, verbose_name='orden')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('internal_name', models.CharField(max_length=200)),
                ('description', models.TextField(verbose_name='descripción')),
                ('price', models.IntegerField(verbose_name='precio de venta')),
                ('purchase_available', models.BooleanField(default=False, verbose_name='disponible venta individual')),
                ('activities', models.ManyToManyField(to='bigbox.Activity')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bigbox.Category', verbose_name='categoría')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bigbox.Category', verbose_name='categoría'),
        ),
        migrations.AddField(
            model_name='activity',
            name='reasons',
            field=models.ManyToManyField(blank=True, to='bigbox.Reason', verbose_name='tags'),
        ),
    ]
