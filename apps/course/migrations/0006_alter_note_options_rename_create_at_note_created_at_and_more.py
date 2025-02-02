# Generated by Django 4.2 on 2024-10-04 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_rename_create_at_course_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['created_at', 'title'], 'verbose_name': 'Anotação', 'verbose_name_plural': 'Anotações'},
        ),
        migrations.RenameField(
            model_name='note',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='note',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
