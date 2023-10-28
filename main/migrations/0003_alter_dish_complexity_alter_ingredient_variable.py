# Generated by Django 4.2.4 on 2023-10-20 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_dish_complexity_alter_ingredient_variable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='complexity',
            field=models.CharField(choices=[('Легко', 'Легко'), ('Нормально', 'Нормально'), ('Складно', 'Складно')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='variable',
            field=models.CharField(choices=[('кг', 'кг'), ('г', 'г'), ('л', 'л'), ('мл', 'мл'), ('шт', 'шт'), ('ч.л', 'ч.л'), ('ст.л', 'ст.л')], max_length=50),
        ),
    ]
