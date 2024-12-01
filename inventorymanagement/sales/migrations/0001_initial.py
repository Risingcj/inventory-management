# Generated by Django 5.0 on 2024-11-26 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('total_sales', models.DecimalField(decimal_places=2, max_digits=10)),
                ('business_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.businessunit')),
            ],
        ),
    ]