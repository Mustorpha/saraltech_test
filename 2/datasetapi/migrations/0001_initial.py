# Generated by Django 4.0.10 on 2024-03-30 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=5, default=0.0, max_digits=10)),
                ('quantity', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('Electronics', 'electronics'), ('Apparel', 'apparel'), ('Home & Kitchen', 'home_and_kitchen')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
