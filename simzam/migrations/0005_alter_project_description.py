# Generated by Django 4.1.6 on 2023-06-05 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simzam', '0004_alter_drawing_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(),
        ),
    ]