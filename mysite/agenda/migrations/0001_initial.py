# Generated by Django 2.1.5 on 2019-01-05 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
    ]
