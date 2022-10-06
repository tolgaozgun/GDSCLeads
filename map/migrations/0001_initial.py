# Generated by Django 4.1.1 on 2022-09-27 19:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(81)])),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('photo', models.ImageField(default='community/avatar.png', null=True, upload_to='community')),
                ('biography', models.TextField()),
                ('social_instagram', models.CharField(blank=True, max_length=300, null=True)),
                ('social_website', models.CharField(blank=True, max_length=300, null=True)),
                ('social_facebook', models.CharField(blank=True, max_length=300, null=True)),
                ('social_twitter', models.CharField(blank=True, max_length=300, null=True)),
                ('social_linkedin', models.CharField(blank=True, max_length=300, null=True)),
                ('social_email', models.CharField(blank=True, max_length=300, null=True)),
                ('social_youtube', models.CharField(blank=True, max_length=300, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='map.city')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('photo', models.ImageField(default='event/avatar.png', null=True, upload_to='event')),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='map.city')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='map.community')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('photo', models.ImageField(default='lead/avatar.png', null=True, upload_to='lead')),
                ('biography', models.TextField()),
                ('social_instagram', models.CharField(blank=True, max_length=300, null=True)),
                ('social_website', models.CharField(blank=True, max_length=300, null=True)),
                ('social_facebook', models.CharField(blank=True, max_length=300, null=True)),
                ('social_twitter', models.CharField(blank=True, max_length=300, null=True)),
                ('social_linkedin', models.CharField(blank=True, max_length=300, null=True)),
                ('social_email', models.CharField(blank=True, max_length=300, null=True)),
                ('social_youtube', models.CharField(blank=True, max_length=300, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_lead', models.BooleanField(default=False)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead', to='map.community')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
