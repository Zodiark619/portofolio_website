# Generated by Django 4.0.1 on 2022-01-30 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meong2', '0002_faction_alter_waifu_faction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waifu',
            name='faction',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bolo2', to='meong2.faction'),
        ),
    ]
