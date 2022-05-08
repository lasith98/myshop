# Generated by Django 4.0.3 on 2022-05-08 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=250)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('nic', models.CharField(max_length=250)),
                ('bank', models.CharField(max_length=250)),
                ('pay_period', models.CharField(max_length=250)),
                ('tax_no', models.CharField(max_length=250)),
                ('basic_salary', models.IntegerField()),
                ('dedcutions', models.IntegerField()),
                ('net_salary', models.IntegerField()),
            ],
        ),
    ]
