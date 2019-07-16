import subprocess

def upload_file(path:str, folder_id:str):
    subprocess.call()


def upload_folder(path:str, folder_id:str):
    command = 'gdrive upload --recursive -p parent_id path'.split(' ')
    return subprocess.check_output(command)

def sync_folder(path:str, folder_id:str):
    
