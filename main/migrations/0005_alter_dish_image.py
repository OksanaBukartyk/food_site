# Generated by Django 4.2.4 on 2023-10-25 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_ingredient_dish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
