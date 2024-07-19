# Generated by Django 2.1.3 on 2018-12-06 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_auto_20181202_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='image_height',
            field=models.PositiveIntegerField(editable=False, null=True, verbose_name='Image Height'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='image_width',
            field=models.PositiveIntegerField(editable=False, null=True, verbose_name='Image Width'),
        ),
    ]
