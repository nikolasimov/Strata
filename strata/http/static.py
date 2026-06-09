import os
import mimetypes


class StaticFileHandler:
    def __init__(self, base_dir="public"):
        self.base_dir = os.path.abspath(base_dir)

    def get_file(self, path):
        # 1. root route mapping
        if path == "/":
            path = "/index.html"

        # 2. build full path
        full_path = os.path.join(self.base_dir, path.lstrip("/"))
        full_path = os.path.abspath(full_path)

        # 3. security check
        if not full_path.startswith(self.base_dir):
            return None, None

        # 4. file existence check
        if not os.path.exists(full_path):
            return None, None

        # 5. read file
        with open(full_path, "rb") as f:
            content = f.read()

        # 6. mime type
        content_type, _ = mimetypes.guess_type(full_path)
        if content_type is None:
            content_type = "text/plain"
            
        print("STATIC REQUEST:", path)
        print("FULL PATH:", full_path)

        return content, content_type