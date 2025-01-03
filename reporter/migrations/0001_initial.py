# Generated by Django 5.1.3 on 2024-11-22 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(choices=[('pothole', 'Pothole'), ('speed_breaker', 'Unmarked Speed-breaker'), ('standing_water', 'Standing Water')], max_length=20)),
                ('location_lat', models.FloatField(help_text='Latitude of the issue location')),
                ('location_lon', models.FloatField(help_text='Longitude of the issue location')),
                ('reported_at', models.DateTimeField(auto_now_add=True, help_text='Date and time when the report was created')),
                ('is_resolved', models.BooleanField(default=False, help_text='Status of the report: Resolved or Not')),
                ('image', models.ImageField(blank=True, help_text='Upload an image of the issue', null=True, upload_to='reports/images/')),
            ],
        ),
    ]
