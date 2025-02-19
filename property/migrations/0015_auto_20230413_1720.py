# Generated by Django 2.2.24 on 2023-04-13 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20230413_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='text_of_complaint',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='complaint_the_apartment',
        ),
        migrations.AddField(
            model_name='complaint',
            name='apartment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='property.Flat', verbose_name='Квартира, на которую жалуются:'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Кто жаловался:'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул:'),
        ),
    ]
