# Generated by Django 4.2.6 on 2023-11-08 10:17

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
        ("blog", "0003_remove_blogpostpage_featured_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReceipePostPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("blog_post_title", models.CharField(blank=True, max_length=200)),
                ("body", wagtail.fields.RichTextField(blank=True)),
                ("date_published", models.DateTimeField()),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
