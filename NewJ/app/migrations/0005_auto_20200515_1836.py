# Generated by Django 3.0.5 on 2020-05-15 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_man_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='man',
            name='slug',
            field=models.SlugField(blank=True, default=None, unique=True),
        ),
        migrations.CreateModel(
            name='AuthCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_code', models.IntegerField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
