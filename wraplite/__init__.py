import os
from wraplite import exceptions
from wraplite.database import Database
from wraplite.table import TableFormat

def get(name: str, folder_path: str = None, error_if_exist: bool = False) -> bool:
    if folder_path is None:
        folder_path = './'

    if not os.path.isdir(folder_path):
        raise exceptions.FolderNotExistError()

    database_path = os.path.join(folder_path, name + '.db')

    if error_if_exist:
        if os.path.exists(database_path):
            raise exceptions.DatabaseExistError()

    return Database(name, folder_path)