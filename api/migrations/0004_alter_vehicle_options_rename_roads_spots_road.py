# Generated by Django 4.0.4 on 2023-01-02 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_counting_traffic_countings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'ordering': ['-created', '-updated']},
        ),
        migrations.RenameField(
            model_name='spots',
            old_name='Roads',
            new_name='Road',
        ),
    ]
