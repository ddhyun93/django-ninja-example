# Generated by Django 4.0.6 on 2022-08-04 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('hospital_name', models.CharField(max_length=128)),
                ('department', models.CharField(max_length=4)),
                ('non_paid_object', models.CharField(blank=True, max_length=64, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN', 'Sunday')], max_length=3)),
                ('is_workingday', models.BooleanField(default=True)),
                ('work_start_time', models.TimeField(default='09:00')),
                ('work_end_time', models.TimeField(default='17:00')),
                ('break_start_time', models.TimeField(default='00:00')),
                ('break_end_time', models.TimeField(default='00:00')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='DiagnosisRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('request_at', models.DateTimeField()),
                ('request_expired_at', models.DateTimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnosis', to='healthcare.doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnosis', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
