# Generated by Django 4.1.3 on 2023-03-31 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_create_nuevo_card_img_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_nuevo_curso',
            name='form_carga_curso',
            field=models.CharField(default='SOME STRING', max_length=250),
        ),
        migrations.AddField(
            model_name='create_nuevo_curso',
            name='img_curso',
            field=models.CharField(default='SOME STRING', max_length=300),
        ),
        migrations.AlterField(
            model_name='create_nuevo_card',
            name='img_card',
            field=models.FileField(default='SOME STRING', upload_to='media/'),
        ),
    ]