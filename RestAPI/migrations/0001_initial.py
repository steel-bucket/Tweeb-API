# Generated by Django 4.1.13 on 2024-03-31 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tlink', models.CharField(max_length=255)),
                ('wlink', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField()),
                ('spreadfactor', models.FloatField()),
                ('hiringchance', models.FloatField()),
                ('source', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('hashtags', models.JSONField()),
                ('location', models.CharField(default=None, max_length=100)),
                ('verified', models.BooleanField()),
            ],
            options={
                'db_table': 'Finalized_Tweets',
            },
        ),
    ]
