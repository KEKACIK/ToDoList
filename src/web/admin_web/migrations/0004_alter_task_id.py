# Generated by Django 4.2.2 on 2023-06-18 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_web', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
