# Generated by Django 2.1.5 on 2019-02-28 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0025_auto_20190227_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
