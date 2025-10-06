import os
import jawa

def read_all_files(path):
    file_contents = []
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.class'):
                try:
                    with open(file_path, 'rb') as f:
                        classfile = jawa.Classfile.parse(f)
                        file_contents.append(f"{file}|{root}\n|Classfile (jawa):\n{classfile}")
                except Exception as e:
                    file_contents.append(f"{file}|{root}\n|Error reading class file with jawa: {e}. Attempting normal read.")
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            file_contents.append(f"{file}|{root}\n|{content}")
                    except Exception as e_normal:
                        file_contents.append(f"{file}|{root}\n|Error reading file normally: {e_normal}")
            else:
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        file_contents.append(f"{file}|{root}\n|{content}")
                except Exception as e:
                    file_contents.append(f"{file}|{root}\n|Error reading file: {e}")
    return "\n\n".join(file_contents)
