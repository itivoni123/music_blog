# Generated by Django 3.1.5 on 2021-02-09 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicblog', '0011_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet1',
            field=models.CharField(default='a', max_length=255),
            preserve_default=False,
        ),
    ]
