# Generated by Django 2.1.5 on 2019-03-11 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='god',
            name='use_for',
            field=models.TextField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
