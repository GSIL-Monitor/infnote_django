# Generated by Django 2.1.5 on 2019-01-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('avatar', models.CharField(max_length=255, null=True)),
                ('bio', models.CharField(max_length=255, null=True)),
                ('signature', models.CharField(max_length=100, null=True)),
                ('topics', models.IntegerField(default=0)),
                ('replies', models.IntegerField(default=0)),
                ('date_created', models.IntegerField(default=0)),
                ('block_height', models.IntegerField(default=0)),
                ('block_time', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'infnote_users',
            },
        ),
    ]