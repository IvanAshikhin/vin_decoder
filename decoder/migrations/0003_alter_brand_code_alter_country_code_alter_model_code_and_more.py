# Generated by Django 4.2.7 on 2023-11-28 05:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "decoder",
            "0002_alter_brand_code_alter_brand_name_alter_country_code_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="code",
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name="country",
            name="code",
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name="model",
            name="code",
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name="year",
            name="code",
            field=models.CharField(max_length=4),
        ),
    ]
