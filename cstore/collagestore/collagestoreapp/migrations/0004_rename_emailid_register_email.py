# Generated by Django 4.1.3 on 2023-03-16 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collagestoreapp', '0003_rename_email_register_emailid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='emailid',
            new_name='email',
        ),
    ]