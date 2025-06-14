# Generated by Django 3.1.1 on 2020-09-08 00:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_addratingfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.restaurant'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('user', 'restaurant')},
        ),
    ]
