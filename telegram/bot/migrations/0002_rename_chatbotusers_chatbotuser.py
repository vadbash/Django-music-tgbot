# Generated by Django 3.2.10 on 2023-12-12 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChatbotUsers',
            new_name='ChatbotUser',
        ),
    ]
