# Generated by Django 4.2 on 2024-10-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_note_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='subject',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
