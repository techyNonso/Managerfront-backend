# Generated by Django 3.1 on 2020-08-26 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('branches', '0003_auto_20200824_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='userId',
        ),
        migrations.AddField(
            model_name='branch',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]