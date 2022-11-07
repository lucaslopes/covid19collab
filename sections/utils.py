from pathlib import Path


def get_path(dir_name, file_name):
  return f'{Path.home()}/Databases/{dir_name}/{file_name}'