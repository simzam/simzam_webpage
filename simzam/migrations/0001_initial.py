# Generated by Django 4.2.2 on 2023-07-02 15:32

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drawing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='tittel')),
                ('text', models.TextField()),
                ('published_date', models.DateField(default=django.utils.timezone.now, verbose_name='publisert')),
                ('drawing', models.ImageField(upload_to='drawing', verbose_name='Tegning')),
                ('small_image', models.ImageField(blank=True, upload_to='drawing/', verbose_name='Liten tegning')),
                ('medium_image', models.ImageField(blank=True, upload_to='drawing', verbose_name='Medium tegning')),
                ('large_image', models.ImageField(blank=True, upload_to='drawing', verbose_name='Stor tegning')),
                ('background_color', models.CharField(default='#FFFFFF', max_length=7)),
            ],
            options={
                'db_table': 'drawing',
            },
        ),
    ]
