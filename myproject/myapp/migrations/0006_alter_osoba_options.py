# Generated by Django 5.1.3 on 2024-11-15 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_ahe_person_age_osoba_data_dodania'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'verbose_name_plural': 'Osoby'},
        ),
    ]