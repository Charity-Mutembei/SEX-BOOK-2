# Generated by Django 4.0.5 on 2022-06-23 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sexbook', '0004_rename_message_message_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sexbook.room'),
        ),
    ]
