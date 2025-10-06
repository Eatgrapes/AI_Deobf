
import os

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return f"Content of {file_path}:\n{content}"
    except Exception as e:
        return f"Error reading file {file_path}: {e}"

