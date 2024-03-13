# by Lucia Pintor
import os, stat


def create_missing_folder(folder_name, change_owner=False):
    """
    This function create a folder if it does not exist.
    :param folder_name:
    :return:
    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    if change_owner is True:
        os.chmod(folder_name, stat.S_IRWXO)

    return folder_name
