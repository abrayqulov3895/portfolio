# Generated by Django 4.1.1 on 2022-09-10 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_information_icon_remove_information_link_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='location',
            field=models.URLField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialistinformation',
            name='percentage',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
