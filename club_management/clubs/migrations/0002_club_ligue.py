# Generated by Django 2.1.7 on 2019-07-25 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='ligue',
            field=models.CharField(default='laliga', max_length=50),
            preserve_default=False,
        ),
    ]
