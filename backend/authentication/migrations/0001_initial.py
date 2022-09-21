# Generated by Django 4.0.7 on 2022-09-01 04:49

import authentication.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='public identifier')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('image', models.CharField(blank=True, max_length=255)),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_resident', models.BooleanField(default=False, verbose_name='resident')),
                ('is_security', models.BooleanField(default=False, verbose_name='security')),
                ('is_supervisor', models.BooleanField(default=False, verbose_name='supervisor')),
                ('is_residenceadmin', models.BooleanField(default=False, verbose_name='residence admin')),
                ('is_condoadmin', models.BooleanField(default=False, verbose_name='condo admin')),
                ('is_agencyadmin', models.BooleanField(default=False, verbose_name='agency admin')),
                ('is_platformadmin', models.BooleanField(default=False, verbose_name='platform admin')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser')),
                ('last_login', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='last login')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created date')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', authentication.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AgencyAdmin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Agency Admin',
                'verbose_name_plural': 'Agency Admins',
                'db_table': 'agency_admin',
            },
        ),
        migrations.CreateModel(
            name='CondoAdmin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Condo Admin',
                'verbose_name_plural': 'Condo Admins',
                'db_table': 'condo_admin',
            },
        ),
        migrations.CreateModel(
            name='PlatformAdmin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Platform Admin',
                'verbose_name_plural': 'Platform Admins',
                'db_table': 'platform_admin',
            },
        ),
        migrations.CreateModel(
            name='ResidenceAdmin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Residence Admin',
                'verbose_name_plural': 'Residence Admins',
                'db_table': 'residence_admin',
            },
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Resident',
                'verbose_name_plural': 'Residents',
                'db_table': 'resident',
            },
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Security',
                'verbose_name_plural': 'Securities',
                'db_table': 'security',
            },
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Supervisor',
                'verbose_name_plural': 'Supervisors',
                'db_table': 'supervisor',
            },
        ),
    ]
