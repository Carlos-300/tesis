# Generated by Django 4.1.3 on 2023-05-05 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_create_new_consultas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_nuevo_card',
            name='img_card',
            field=models.ImageField(blank=True, null=True, upload_to='img/carta'),
        ),
        migrations.AlterField(
            model_name='create_nuevo_curso',
            name='img_curso',
            field=models.ImageField(blank=True, null=True, upload_to='img/cursos'),
        ),
        migrations.AlterField(
            model_name='create_nuevo_publicacion',
            name='img_pub',
            field=models.ImageField(blank=True, null=True, upload_to='img/publicidad'),
        ),
    ]
