# Generated by Django 4.1.3 on 2022-11-09 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, help_text='Aciklama Yazin', null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(help_text='Kurs adini yaziniz', max_length=200, unique=True),
        ),
    ]