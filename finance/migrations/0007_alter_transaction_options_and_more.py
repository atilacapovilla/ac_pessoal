# Generated by Django 4.2 on 2024-08-05 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_category_method_alter_category_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-transaction_date', 'due_date', 'type'], 'verbose_name': 'Transação', 'verbose_name_plural': 'Transações'},
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='payment_date',
        ),
    ]