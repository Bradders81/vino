# Generated by Django 3.2 on 2022-05-01 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_userreview_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreview',
            name='score',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (4, '5')], default=1),
        ),
    ]