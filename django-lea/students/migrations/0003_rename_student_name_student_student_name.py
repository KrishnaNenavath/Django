# Generated by Django 5.0.2 on 2024-03-05 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_student_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Student_name',
            new_name='student_name',
        ),
    ]
