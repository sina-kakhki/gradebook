# Generated by Django 4.2.1 on 2023-05-20 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradebook', '0002_remove_studentenrollment_classid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='classID',
            field=models.CharField(default=1, max_length=8),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='staffID',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentID',
            field=models.CharField(max_length=6),
        ),
    ]