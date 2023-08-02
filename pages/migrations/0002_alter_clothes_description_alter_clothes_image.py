# Generated by Django 4.2.2 on 2023-07-16 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d'),
        ),
    ]