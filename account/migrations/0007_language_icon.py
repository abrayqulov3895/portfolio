# Generated by Django 4.1.1 on 2022-09-10 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_brend_fair_price_language_love_to_thoughts_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='icon',
            field=models.CharField(choices=[('ldInner profLevel1', 'ldInner profLevel1'), ('ldInner profLevel2', 'ldInner profLevel2'), ('ldInner profLevel3', 'ldInner profLevel3'), ('ldInner profLevel4', 'ldInner profLevel4'), ('ldInner profLevel5', 'ldInner profLevel5'), ('ldInner profLevel6', 'ldInner profLevel6'), ('ldInner profLevel7', 'ldInner profLevel7'), ('ldInner profLevel8', 'ldInner profLevel8'), ('ldInner profLevel9', 'ldInner profLevel9'), ('ldInner profLevel10', 'ldInner profLevel10')], default=1, max_length=150),
            preserve_default=False,
        ),
    ]