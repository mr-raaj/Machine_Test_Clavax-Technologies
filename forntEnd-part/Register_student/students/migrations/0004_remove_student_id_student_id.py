# Generated by Django 4.1.2 on 2023-09-21 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AddField(
            model_name='student',
            name='ID',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
