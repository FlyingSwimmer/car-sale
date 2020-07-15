# Generated by Django 3.0.8 on 2020-07-11 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sale.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('car_name', models.CharField(max_length=64)),
                ('car_model', models.CharField(max_length=64)),
                ('min_price', models.PositiveIntegerField()),
                ('end_time', models.DateTimeField(default=sale.models.default_end_time)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ads', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.Advertisement')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
