import os
import datetime
def filter_by_mtime(file_paths, datetime_th):
    timestamp_th = datetime_th.timestamp()
    return [ path for path in file_paths if os.path.getmtime(path) < timestamp_th ]

def list_files(raw_path):
    path = raw_path if raw_path[-1] != '/' else raw_path[0:-1]
    if os.path.isdir(path):
        child_paths = [ path + '/' + file for file in os.listdir(path)]
        file_paths = [ path for path in child_paths if os.path.isfile(path)]
    elif os.path.isfile(path):
        file_paths = [path]
    else:
        file_paths = []
    return file_paths

def delete_paths(paths):
    for path in paths:
        try:
            os.remove(path)
            print('remove {} success.'.format(path))
        except Exception as e:
            print(e)
            print('error, skip {}'.format(path))

def delete_outdated(dir_paths, datetime_th=None, dry=True):
    if datetime_th is None:
        datetime_th = datetime.datetime.now() - datetime.timedelta(days=7)
    all_paths = []
    for dir_path in dir_paths:
        all_paths += list_files(dir_path)
    outdated_paths = filter_by_mtime(all_paths, datetime_th)
    if dry:
        print(outdated_paths)
    else:
        delete_paths(outdated_paths)
