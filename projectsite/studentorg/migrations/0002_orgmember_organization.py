# Generated by Django 5.0.3 on 2024-04-02 08:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentorg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgmember',
            name='Organization',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='studentorg.organization'),
            preserve_default=False,
        ),
    ]
