# Generated by Django 4.2.7 on 2023-11-23 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decoder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='model',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]