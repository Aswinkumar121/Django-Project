# Generated by Django 5.0 on 2024-01-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0005_customuser_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='roles',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_expense_admin',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_expense_creator',
            field=models.BooleanField(default=False),
        ),
    ]
