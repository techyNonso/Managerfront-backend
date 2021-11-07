# Generated by Django 3.1 on 2020-08-26 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0002_auto_20200824_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='userId',
        ),
        migrations.AddField(
            model_name='company',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]