# Generated by Django 3.2 on 2022-02-10 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220210_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='image',
            field=models.ImageField(blank=True, default='images/placeholder.png', null=True, upload_to=''),
        ),
    ]