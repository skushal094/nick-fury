# Generated by Django 3.0.7 on 2020-06-23 19:53

from django.conf import settings
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('Client', 'Client'), ('Therapist', 'Therapist')], max_length=255)),
                ('journal', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_access', models.BooleanField(default=False)),
                ('journal_requested', models.CharField(choices=[('Approved', 'Approved'), ('Declined', 'Declined'), ('Pending', 'Pending'), ('Not Requested', 'Not Requested')], default='Not Requested', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('client', models.ForeignKey(limit_choices_to={'type': 'Client'}, on_delete=django.db.models.deletion.CASCADE, related_name='mapping_client', to=settings.AUTH_USER_MODEL)),
                ('therapist', models.ForeignKey(limit_choices_to={'type': 'Therapist'}, on_delete=django.db.models.deletion.CASCADE, related_name='mapping_therapist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_note', models.CharField(blank=True, max_length=255, null=True)),
                ('shared_note', models.CharField(blank=True, max_length=255, null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Declined', 'Declined')], default='Pending', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('mapping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session_mapping', to='therapy_app.Mapping')),
            ],
        ),
        migrations.CreateModel(
            name='MappingRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Declined', 'Declined')], default='Pending', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_who', to=settings.AUTH_USER_MODEL)),
                ('whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_whom', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emotion', models.CharField(choices=[('Happiness', 'Happiness'), ('Caring', 'Caring'), ('Depression', 'Depression'), ('Inadequate', 'Inadequate'), ('Fear', 'Fear'), ('Confusion', 'Confusion'), ('Hurt', 'Hurt'), ('Anger', 'Anger'), ('Loneliness', 'Loneliness'), ('Remorse', 'Remorse')], max_length=255)),
                ('intensity', models.CharField(choices=[('Strong', 'Strong'), ('Medium', 'Medium'), ('Light', 'Light')], max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('client', models.ForeignKey(limit_choices_to={'type': 'Client'}, on_delete=django.db.models.deletion.CASCADE, related_name='emotion_client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_from', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
