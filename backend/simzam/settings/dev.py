from .base import *


DEBUG = env.bool("DEBUG", default=False)


SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])

FRONTEND_DIR = os.path.abspath(os.path.join(BASE_DIR, "../frontend/"))
WEBPACK_BUNDLE_DIR = os.path.join(FRONTEND_DIR, "assets/webpack_bundles")

USE_AWS_S3 = env.bool("USE_S3", default=True)

if USE_AWS_S3:
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME")
    AWS_DEFAULT_ACL = "public-read"
    AWS_S3_REGION = env.str("AWS_S3_REGION")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

    # FIXME names the folder in the bucket
    AWS_LOCATION = "static"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

else:
    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

    STATICFILES_FINDERS = [
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    ]
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "frontend_assets")]


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

WEBPACK_LOADER = {
    "DEFAULT": {
        # "BUNDLE_DIR_NAME": WEBPACK_BUNDLE_DIR,
        "CACHE": not DEBUG,
        "STATS_FILE": os.path.join(
            BASE_DIR, "frontend_assets/webpack_bundles/webpack-stats.json"
        ),
        "POLL_INTERVAL": 0.1,
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
    }
}


try:
    from .local import *
except ImportError:
    pass
