# Generated by Django 4.2.16 on 2024-11-27 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loginTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('password2', models.CharField(max_length=200, null=True)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tourism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlaceName', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('State', models.CharField(max_length=50)),
                ('District', models.CharField(max_length=100)),
                ('Weather', models.CharField(choices=[('SUNNY', 'Sunny'), ('RAINY', 'Rainy'), ('SNOWY', 'Snowy')], max_length=10)),
                ('Location_Link', models.URLField()),
                ('Destination_Img', models.ImageField(upload_to='tourism_img/')),
                ('Destination_Img1', models.ImageField(blank=True, null=True, upload_to='tourism_img/')),
                ('Destination_Img2', models.ImageField(blank=True, null=True, upload_to='tourism_img/')),
                ('Destination_Img3', models.ImageField(blank=True, null=True, upload_to='tourism_img/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
                ('password2', models.CharField(max_length=200)),
            ],
        ),
    ]
