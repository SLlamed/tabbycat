# Generated by Django 3.0.7 on 2020-07-24 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0016_auto_20200705_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='long_name',
            field=models.CharField(editable=False, help_text='The full name of the team, including institution name. (This is autogenerated.)', max_length=251, verbose_name='long name'),
        ),
        migrations.AlterField(
            model_name='team',
            name='short_name',
            field=models.CharField(editable=False, help_text='The name shown in the draw, including institution name. (This is autogenerated.)', max_length=56, verbose_name='short name'),
        ),
    ]
