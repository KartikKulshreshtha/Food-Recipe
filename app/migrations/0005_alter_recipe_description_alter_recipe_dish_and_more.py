# Generated by Django 4.0.1 on 2022-01-23 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_recipe_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(blank=True, max_length=1000000000000000000000000, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='dish',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(blank=True, max_length=1000000000000000000000000, null=True),
        ),
    ]
