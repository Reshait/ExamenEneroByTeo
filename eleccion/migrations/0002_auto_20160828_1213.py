# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eleccion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='circunscripcion',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='mesa',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='partido',
            options={'ordering': ['nombre']},
        ),
    ]
