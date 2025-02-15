# Generated by Django 5.0.7 on 2024-08-26 02:00

import django.db.models.deletion
import main.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url_identifier', models.CharField(blank=True, editable=False, max_length=36, unique=True)),
                ('banner', models.ImageField(blank=True, null=True, upload_to=main.models.banner_upload_path)),
                ('icon', models.ImageField(blank=True, null=True, upload_to=main.models.icon_upload_path)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(default='src/static/images/default/image.png', upload_to=main.models.category_image_upload_path)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='main.business')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='items/')),
                ('vegan', models.BooleanField(default=False)),
                ('sin_tacc', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='main.category')),
            ],
        ),
    ]
