# Generated by Django 4.2.4 on 2023-10-23 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_dish_complexity_alter_ingredient_variable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='dish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='main.dish'),
        ),
    ]
