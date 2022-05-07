# Generated by Django 4.0.3 on 2022-05-07 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_sheet_id', models.CharField(max_length=1)),
                ('date', models.DateField()),
                ('liabilities', models.FloatField()),
                ('equity', models.FloatField()),
                ('asset', models.FloatField()),
            ],
        ),
    ]