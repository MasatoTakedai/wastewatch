# Generated by Django 4.2.11 on 2024-04-20 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wastewatch', '0004_alter_report_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(help_text='Select the time of the report'),
        ),
    ]