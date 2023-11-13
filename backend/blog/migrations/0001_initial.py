# Generated by Django 4.2.6 on 2023-11-13 16:10

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogIndexPage",
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
                ("intro", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="BlogPostPage",
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
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            ("heading", wagtail.blocks.CharBlock()),
                            (
                                "image",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "title",
                                            wagtail.blocks.CharBlock(required=False),
                                        ),
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(),
                                        ),
                                        (
                                            "alt",
                                            wagtail.blocks.CharBlock(require=False),
                                        ),
                                    ],
                                    required=False,
                                ),
                            ),
                            ("text", wagtail.blocks.TextBlock(required=False)),
                        ],
                        blank=True,
                        null=True,
                        use_json_field=True,
                    ),
                ),
                ("date_published", models.DateTimeField()),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
