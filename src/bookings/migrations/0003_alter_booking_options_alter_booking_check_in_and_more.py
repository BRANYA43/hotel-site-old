# Generated by Django 5.0 on 2024-01-03 01:44

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('bookings', '0002_rename_is_children_booking_has_children'),
        ('rooms', '0003_alter_room_options_alter_roomdata_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-created'], 'verbose_name': 'Бронювання', 'verbose_name_plural': 'Бронювання'},
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(verbose_name='Дата заїзду'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(verbose_name='Дата виїзду'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='has_children',
            field=models.BooleanField(default=False, verbose_name='Чи є діти'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Оплачено'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='persons',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Кількість осіб'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='rooms',
            field=models.ManyToManyField(to='rooms.room', verbose_name='Номери'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='type',
            field=models.PositiveSmallIntegerField(
                choices=[(0, 'Economy'), (1, 'Standard'), (2, 'Deluxe'), (3, 'Luxe')], default=1, verbose_name='Тип'
            ),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Користувач'
            ),
        ),
        migrations.AlterField(
            model_name='booking',
            name='uuid',
            field=models.UUIDField(
                default=uuid.uuid4,
                primary_key=True,
                serialize=False,
                unique=True,
                verbose_name='Унікальний ідентифікатор',
            ),
        ),
    ]
