import zipfile
import os

def unzip(file_path, output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
        return f"Successfully extracted {file_path} to {output_dir}"
    except Exception as e:
        return f"Error extracting file: {e}"