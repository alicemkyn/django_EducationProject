# Generated by Django 4.1.3 on 2022-11-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, to='courses.tag'),
        ),
    ]
