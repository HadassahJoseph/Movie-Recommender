# Generated by Django 5.1.1 on 2024-09-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdb_id', models.CharField(max_length=48)),
                ('genres', models.CharField(max_length=200, null=True)),
                ('original_language', models.CharField(max_length=20, null=True)),
                ('original_title', models.CharField(max_length=500)),
                ('release_date', models.IntegerField(default=1970)),
                ('overview', models.TextField(max_length=2000, null=True)),
                ('vote_average', models.FloatField(default=0)),
                ('vote_count', models.IntegerField(default=0)),
                ('poster_path', models.CharField(max_length=64, null=True)),
                ('watched', models.BooleanField(default=False, null=True)),
                ('recommended', models.BooleanField(default=False, null=True)),
            ],
        ),
    ]
