# Generated by Django 5.1.6 on 2025-03-15 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_contact_email_alter_contact_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.CharField(max_length=16),
        ),
    ]
