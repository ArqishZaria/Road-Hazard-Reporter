# Generated by Django 5.1.3 on 2024-12-01 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0003_alter_report_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='priority',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=1, help_text='Priority of the report (1-10)'),
        ),
    ]