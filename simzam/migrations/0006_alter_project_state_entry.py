# Generated by Django 4.1.6 on 2023-06-06 09:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('simzam', '0005_alter_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='state',
            field=models.CharField(choices=[('SKETCHED', 'På tapetet'), ('TODO', 'På bordet'), ('HOLD', 'I skuffen'), ('DONE', 'I arkivet')], default='SKETCHED', max_length=30, verbose_name='tilstand'),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('published_date', models.DateField(default=django.utils.timezone.now, verbose_name='date published')),
                ('slug', models.SlugField(blank=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='simzam.project')),
            ],
        ),
    ]