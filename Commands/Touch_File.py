
import os

def touch(path):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'a'):
            os.utime(path, None)
        return f"Successfully created file: {path}"
    except Exception as e:
        return f"Error creating file: {e}"
