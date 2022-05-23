# Generated by Django 4.0.4 on 2022-05-23 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Death',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=0, max_length=100)),
                ('location', models.CharField(max_length=30)),
                ('deathcnt', models.IntegerField(default=0)),
                ('incdec', models.IntegerField(default=0)),
                ('defCnt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Patientadd',
            fields=[
                ('date', models.DateTimeField(default=0, max_length=100, primary_key=True, serialize=False)),
                ('gangnam', models.IntegerField(default=0)),
                ('gangdong', models.IntegerField(default=0)),
                ('gangbuk', models.IntegerField(default=0)),
                ('gangseo', models.IntegerField(default=0)),
                ('gwanak', models.IntegerField(default=0)),
                ('gwangjin', models.IntegerField(default=0)),
                ('guro', models.IntegerField(default=0)),
                ('geumcheon', models.IntegerField(default=0)),
                ('nowon', models.IntegerField(default=0)),
                ('dobong', models.IntegerField(default=0)),
                ('ddm', models.IntegerField(default=0)),
                ('dongjak', models.IntegerField(default=0)),
                ('mapo', models.IntegerField(default=0)),
                ('sdm', models.IntegerField(default=0)),
                ('seocho', models.IntegerField(default=0)),
                ('seongdong', models.IntegerField(default=0)),
                ('seongbuk', models.IntegerField(default=0)),
                ('songpa', models.IntegerField(default=0)),
                ('yangcheon', models.IntegerField(default=0)),
                ('ydp', models.IntegerField(default=0)),
                ('yongsan', models.IntegerField(default=0)),
                ('ep', models.IntegerField(default=0)),
                ('jongno', models.IntegerField(default=0)),
                ('junggu', models.IntegerField(default=0)),
                ('jungnang', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Patientsum',
            fields=[
                ('date', models.DateTimeField(default=0, max_length=100, primary_key=True, serialize=False)),
                ('gangnam', models.IntegerField(default=0)),
                ('gangdong', models.IntegerField(default=0)),
                ('gangbuk', models.IntegerField(default=0)),
                ('gangseo', models.IntegerField(default=0)),
                ('gwanak', models.IntegerField(default=0)),
                ('gwangjin', models.IntegerField(default=0)),
                ('guro', models.IntegerField(default=0)),
                ('geumcheon', models.IntegerField(default=0)),
                ('nowon', models.IntegerField(default=0)),
                ('dobong', models.IntegerField(default=0)),
                ('ddm', models.IntegerField(default=0)),
                ('dongjak', models.IntegerField(default=0)),
                ('mapo', models.IntegerField(default=0)),
                ('sdm', models.IntegerField(default=0)),
                ('seocho', models.IntegerField(default=0)),
                ('seongdong', models.IntegerField(default=0)),
                ('seongbuk', models.IntegerField(default=0)),
                ('songpa', models.IntegerField(default=0)),
                ('yangcheon', models.IntegerField(default=0)),
                ('ydp', models.IntegerField(default=0)),
                ('yongsan', models.IntegerField(default=0)),
                ('ep', models.IntegerField(default=0)),
                ('jongno', models.IntegerField(default=0)),
                ('junggu', models.IntegerField(default=0)),
                ('jungnang', models.IntegerField(default=0)),
            ],
        ),
    ]
