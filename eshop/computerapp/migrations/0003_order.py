# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-06 10:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('computerapp', '0002_deliveryaddress_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('0', 'new'), ('1', 'not paid'), ('2', 'paid'), ('3', 'transport'), ('4', 'closed')], default='0', max_length=2)),
                ('remark', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_address', to='computerapp.DeliveryAddress')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_product', to='computerapp.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_of', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
