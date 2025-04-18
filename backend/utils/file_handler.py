import os
import uuid

UPLOAD_DIR = "functions"

def save_function_file(file, language):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_ext = "py" if language == "python" else "js"
    filename = f"{uuid.uuid4()}.{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return file_path
