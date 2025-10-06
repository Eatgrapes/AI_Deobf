import os

def read_all_files(path):
    file_contents = []
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    file_contents.append(f"{file}|{root}\n|{content}")
            except Exception as e:
                file_contents.append(f"{file}|{root}\n|Error reading file: {e}")
    return "\n\n".join(file_contents)
