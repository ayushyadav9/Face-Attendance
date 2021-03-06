# Generated by Django 3.2.6 on 2021-10-24 08:18

from django.db import migrations, models
import django.db.models.deletion
import myapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_profile', serialize=False, to='auth.user')),
                ('face_data', models.JSONField(default=myapp.models.my_default)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
    ]
