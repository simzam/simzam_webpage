#!/usr/bin/env python3

import os
import requests
import django
from django.core.files import File
from django.conf import settings
from django.core.files.storage import default_storage
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "homepage.settings")
django.setup()

from simzam.models import Drawing

fake = Faker()


def generate_placeholder_drawing():
    width = fake.random_int(min=200, max=800)
    height = fake.random_int(min=200, max=600)
    image_url = f"https://picsum.photos/{width}/{height}"
    image_response = requests.get(image_url, stream=True)
    image_response.raise_for_status()
    image_name = os.path.basename(image_url)
    drawings_folder = os.path.join(settings.MEDIA_ROOT, "drawings")
    os.makedirs(drawings_folder, exist_ok=True)
    file_path = os.path.join(drawings_folder, image_name)

    with default_storage.open(file_path, 'wb') as f:
        for chunk in image_response.iter_content(chunk_size=1024):
            f.write(chunk)
    return file_path


def save_drawing_with_placeholder():
    drawing = Drawing(
        title=fake.sentence(),
        text=fake.paragraph()
    )
    placeholder_image_path = generate_placeholder_drawing()
    with default_storage.open(placeholder_image_path, 'rb') as f:
        drawing.drawing.save(os.path.basename(placeholder_image_path), File(f))
    default_storage.delete(placeholder_image_path)
    drawing.save()


if __name__ == '__main__':
    num_drawings = 100  # Adjust the number as per your requirements
    for _ in range(num_drawings):
        save_drawing_with_placeholder()
