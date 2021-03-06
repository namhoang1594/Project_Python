# Generated by Django 2.2.5 on 2021-01-30 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('CategoriesID', models.IntegerField(primary_key=True, serialize=False)),
                ('CategoriesName', models.CharField(max_length=50)),
                ('CategoriesDescription', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'categories',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('ProductsID', models.IntegerField(primary_key=True, serialize=False)),
                ('ProductsName', models.CharField(max_length=50)),
                ('ProductsDescription', models.TextField(max_length=100)),
                ('ProductsPrice', models.DecimalField(decimal_places=10, max_digits=19)),
                ('ProductsNumber', models.IntegerField(default=0)),
                ('ProductsImage', models.ImageField(upload_to=None)),
                ('CategoriesID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productweb.Categories')),
            ],
            options={
                'db_table': 'products',
                'managed': True,
            },
        ),
    ]
