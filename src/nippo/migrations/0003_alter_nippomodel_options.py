# Generated by Django 5.0.7 on 2024-08-02 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nippo', '0002_alter_nippomodel_content_alter_nippomodel_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nippomodel',
            options={'verbose_name': '日報', 'verbose_name_plural': '日報一覧'},
        ),
    ]
