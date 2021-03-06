# Generated by Django 4.0.3 on 2022-04-15 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.UUIDField()),
                ('date', models.DateField()),
                ('reference_no', models.TextField(max_length=50)),
                ('total_amount', models.FloatField()),
                ('remark', models.TextField()),
                ('category', models.CharField(max_length=30)),
                ('account', models.CharField(max_length=39)),
            ],
        ),
    ]
