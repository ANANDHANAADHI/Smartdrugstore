# Generated by Django 4.1.7 on 2023-04-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usregandlog', '0004_alter_register_phone_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='finger_print',
            field=models.ImageField(max_length=10000, upload_to=''),
        ),
    ]
