import os

# settings.pyからそのままコピー
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = "7qoc+r%tz5xb0vd^n5(8_dqvo+7yj7-+nt5e!1j52c+mv!+-+j"

# settings.pyからそのままコピー
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

DEBUG = True  # ローカルでDebugできるようになります
