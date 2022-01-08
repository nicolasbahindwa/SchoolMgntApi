# Generated by Django 4.0.1 on 2022-01-07 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_student', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('preferred_name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(upload_to='profile-images')),
                ('discord_name', models.CharField(max_length=100, null=True)),
                ('github_username', models.CharField(max_length=100)),
                ('codepen_username', models.CharField(max_length=100, null=True)),
                ('fcc_profile_url', models.CharField(max_length=255, null=True)),
                ('current_level', models.IntegerField(choices=[(1, 'Level One'), (2, 'Level Two')], default=1)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('timezone', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]