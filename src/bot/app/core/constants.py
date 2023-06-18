import os
from pathlib import Path

FLOAT_REGEX = r"^\d*[.,]?\d*$"
PHONE_NUMBER_REGEX = r"^([0-9\(\)\/\+ \-]*)$"
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
DATE_FORMAT = "%d-%m-%y"
DATETIME_FORMAT = "%d-%m-%y %H:%M"

DATA_DIR = Path(__file__).parent.parent / "data"
IMAGES_DIR = DATA_DIR / "images"


def get_locales_dir():
    app_dir: Path = Path(os.getcwd())
    locales_dir = app_dir / "locales"
    return locales_dir


def get_files_dir():
    app_dir: Path = Path(os.getcwd())
    locales_dir = app_dir / "files"
    return locales_dir
