# Generated by Django 2.1.2 on 2018-10-26 12:08

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=1000)),
                ('uri', models.CharField(max_length=1000)),
                ('claim_name', models.CharField(max_length=1000)),
                ('outpoint', models.CharField(max_length=1000)),
                ('lbrynet_data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('downloaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]