# Generated by Django 5.0.6 on 2024-08-30 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emp_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="department",
            name="name",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name="employee",
            name="first_name",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name="employee",
            name="last_name",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name="role",
            name="name",
            field=models.CharField(default=None, max_length=100),
        ),
    ]
