import os

def ls(path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            result.append(os.path.join(root, name))
        for name in dirs:
            result.append(os.path.join(root, name))
    return "\n".join(result)
