# Generated by Django 4.1.7 on 2023-03-20 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simzam', '0003_remove_drawing_slug_drawing_text_alter_drawing_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawing',
            name='text',
            field=models.TextField(),
        ),
    ]
