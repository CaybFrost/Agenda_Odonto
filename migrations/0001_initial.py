# Generated by Django 5.0 on 2023-12-30 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('marcado_em', models.DateTimeField(auto_now_add=True)),
                ('data_consulta', models.DateTimeField()),
                ('dentista', models.CharField(max_length=100)),
            ],
        ),
    ]
