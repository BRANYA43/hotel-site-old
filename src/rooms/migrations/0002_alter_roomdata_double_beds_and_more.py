# Generated by Django 5.0 on 2024-01-02 16:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomdata',
            name='double_beds',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='roomdata',
            name='single_beds',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]