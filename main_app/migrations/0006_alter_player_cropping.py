# Generated by Django 5.1.1 on 2024-09-20 22:10

import image_cropping.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_player_cropping_alter_player_player_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('player_img', '271x271', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]