import os
import shutil

def to_relative_path(original_path: str, base_dir: str) -> str:
    path_parts = original_path.split(os.sep)
    
    try:
        index = path_parts.index(base_dir)
    except ValueError:
        raise ValueError(f"'{base_dir}' not found in the path")
    
    relative_path = '.' + os.sep + os.sep.join(path_parts[index:])
    return relative_path

def empty_directory(dir_path):
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                if os.path.basename(file_path) != ".gitignore":
                    os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))