# Generated by Django 4.1.3 on 2023-03-30 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='create_nuevo_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_card', models.CharField(max_length=30)),
                ('cargo_card', models.CharField(max_length=30)),
                ('descrip_card', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='create_nuevo_curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_curso', models.CharField(max_length=30)),
                ('descrip_corta_curso', models.CharField(max_length=30)),
                ('descrip_larga_curso', models.CharField(max_length=30)),
                ('requisitos_curso', models.CharField(max_length=30)),
                ('time_start_curso', models.DateField()),
                ('time_end_curso', models.DateField()),
                ('servicio_curso', models.CharField(max_length=30)),
                ('hospital_curso', models.CharField(max_length=30)),
                ('personal_cursos', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='create_nuevo_publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pub', models.CharField(max_length=30)),
                ('descripcion_pub', models.CharField(max_length=30)),
            ],
        ),
    ]