# Generated by Django 4.0.1 on 2022-01-23 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='dish',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]