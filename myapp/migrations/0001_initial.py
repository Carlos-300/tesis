# Generated by Django 4.1.3 on 2023-06-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('celular', models.IntegerField()),
                ('nombres', models.CharField(default='', max_length=255)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'mi_tabla_usuario',
            },
        ),
        migrations.CreateModel(
            name='create_new_consultas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(max_length=100)),
                ('rut', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('Correo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='create_new_consultas_respondidas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(max_length=70)),
                ('rut', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('Correo', models.CharField(max_length=100)),
                ('fecha_respuesta', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='create_nuevo_card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img_card', models.ImageField(blank=True, null=True, upload_to='img/carta')),
                ('nombre_card', models.CharField(max_length=25)),
                ('cargo_card', models.CharField(max_length=100)),
                ('descrip_card', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='create_nuevo_curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_curso', models.CharField(max_length=100)),
                ('img_curso', models.ImageField(blank=True, null=True, upload_to='img/cursos')),
                ('form_carga_curso', models.FileField(blank=True, null=True, upload_to='documents')),
                ('descrip_corta_curso', models.CharField(max_length=250)),
                ('descrip_larga_curso', models.CharField(max_length=600)),
                ('requisitos_curso', models.CharField(max_length=100)),
                ('time_start_curso', models.DateField()),
                ('time_end_curso', models.DateField()),
                ('servicio_curso', models.CharField(max_length=100)),
                ('hospital_curso', models.CharField(max_length=100)),
                ('personal_cursos', models.CharField(max_length=80)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='create_nuevo_publicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img_pub', models.ImageField(blank=True, null=True, upload_to='img/public')),
                ('nombre_pub', models.CharField(max_length=100)),
                ('descrip_pub', models.CharField(default='SOME STRING', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='new_class_hospital',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_hospital', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='new_class_servicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_sev', models.CharField(max_length=50)),
            ],
        ),
    ]
