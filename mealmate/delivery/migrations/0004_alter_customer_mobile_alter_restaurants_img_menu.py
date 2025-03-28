# Generated by Django 5.1.7 on 2025-03-13 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_rename_image_restaurants_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(default=90, max_length=12),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='img',
            field=models.URLField(default='https://www.foodiesfeed.com/wp-content/uploads/2023/06/burger-with-melted-cheese.jpg'),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('is_available', models.BooleanField(default=True)),
                ('category', models.CharField(max_length=50)),
                ('res', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.restaurants')),
            ],
        ),
    ]
