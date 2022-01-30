# Generated by Django 4.0.1 on 2022-01-30 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meong2', '0003_alter_waifu_faction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waifu',
            name='expansion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bolo_expansion', to='meong2.expansion'),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='faction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bolo2_faction', to='meong2.faction'),
        ),
        migrations.AlterField(
            model_name='waifu',
            name='type',
            field=models.ManyToManyField(related_name='bolo1_type', to='meong2.type'),
        ),
    ]
