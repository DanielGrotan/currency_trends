import os


def get_absolute_path(file_path: str, relative_path: str) -> str:
    return os.path.join(os.path.dirname(os.path.abspath(file_path)), relative_path)
