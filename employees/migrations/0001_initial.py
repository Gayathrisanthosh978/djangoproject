# Generated by Django 4.0.1 on 2022-03-04 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=120)),
                ('department', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('salary', models.PositiveIntegerField()),
                ('experience', models.PositiveIntegerField()),
                ('active_status', models.BooleanField(default=True)),
            ],
        ),
    ]
