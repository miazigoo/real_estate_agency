# Generated by Django 2.2.24 on 2023-04-08 22:00

from django.db import migrations


def create_a_value_for_a_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    new_building_year = 2015
    Flat.objects.filter(construction_year__gte=new_building_year).update(new_building=True)
    Flat.objects.filter(construction_year__lt=new_building_year).update(new_building=False)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(create_a_value_for_a_building),
    ]
