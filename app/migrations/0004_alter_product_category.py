# Generated by Django 3.2.6 on 2021-09-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Healthy_Food', 'Healthy Food'), ('Gym_Box', 'Gym box'), ('TAF', 'Traditional Asian Food'), ('CakesADD', 'Cake and Dessert dishes'), ('OGP', 'Office Gatherings and Parties'), ('Breakfast', 'Breakfast'), ('Vegan', 'Vegan')], max_length=30),
        ),
    ]
