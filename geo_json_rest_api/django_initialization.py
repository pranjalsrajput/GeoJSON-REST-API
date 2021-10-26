import django
import dotenv
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def start_django():
    try:
        dotenv.read_dotenv(os.path.join(ROOT_DIR, ".env"))
    except FileNotFoundError:
        print("No .env file")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
    django.setup()
