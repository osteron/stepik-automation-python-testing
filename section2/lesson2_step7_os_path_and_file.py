import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, file)
element.send_keys(file_path)
