from json import dump, load
from pathlib import Path


def validate_file(file_path: str) -> bool:
    """Verifies the existance of a file with the given path."""

    if Path(file_path).exists():
        return True
    else:
        return False


def read_json(file_path: str) -> dict[str, str]:
    """Reads a file with the given name and returns its content as a string."""

    try:
        content = load(open(file_path))
    except FileNotFoundError:
        return dict()

    return content


def write_json(file_name: str, content: dict[str, str]) -> bool:
    """Writes a given content String into the specified JSON file.\nReturns True when successful."""

    try:
        with open(file_name, "w") as file:
            dump(content, file)
    except Exception:
        print("Failed to write to file.")
        return False

    return True
