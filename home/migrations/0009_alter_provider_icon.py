# Generated by Django 4.1.5 on 2024-01-23 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_provider_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='icon',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
