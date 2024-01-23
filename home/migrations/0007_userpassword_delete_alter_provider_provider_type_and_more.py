# Generated by Django 4.1.5 on 2024-01-23 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_provider_fields_remove_provider_private_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpassword',
            name='delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='provider',
            name='provider_type',
            field=models.CharField(choices=[('1', 'Social'), ('2', 'Media'), ('3', 'Game'), ('4', 'Bank'), ('5', 'Development'), ('6', 'Mail'), ('7', 'Other')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='userpassword',
            name='username',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]