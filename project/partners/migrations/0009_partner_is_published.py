# Generated by Django 2.1.2 on 2019-03-19 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0008_merge_20190307_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Published'),
        ),
    ]