import os
import datetime
from pprint import pprint
def filter_by_mtime(file_paths, datetime_th):
    timestamp_th = datetime_th.timestamp()
    return [ path for path in file_paths if os.path.getmtime(path) < timestamp_th ]

def list_files(raw_path, depth):
    target_path = raw_path if raw_path[-1] != '/' else raw_path[0:-1]
    paths = [target_path]
    for i in range(depth):
        child_paths = []
        for path in paths:
            if os.path.isfile(path):
                child_paths.append(path)
            elif os.path.isdir(path):
                child_paths += [ path + '/' + file for file in os.listdir(path)]
        paths = child_paths

    only_file = [ path for path in paths if os.path.isfile(path)]
    return only_file

    # if os.path.isdir(path):
    #     child_paths = [ path + '/' + file for file in os.listdir(path)]
    #     file_paths = []
    #     for child_path in child_paths:
    #         if os.path.isfile(child_path):
    #             file_paths += child_path
    #         elif dir2 and os.path.isdir(child_path):
    #             grandchildren = [ child_path + '/' + file for file in os.listdir(child_path) ]
    #             file_paths += [ path for path in grandchildren if os.path.isfile(path)]
    # elif os.path.isfile(path):
    #     file_paths = [path]
    # else:
    #     file_paths = []
    # return file_paths

def delete_paths(paths):
    for path in paths:
        try:
            os.remove(path)
            print('remove {} success.'.format(path))
        except Exception as e:
            print(e)
            print('error, skip {}'.format(path))

def delete_outdated(dir_paths, datetime_th=None, dry=True, depth=1):
    if datetime_th is None:
        datetime_th = datetime.datetime.now() - datetime.timedelta(days=7)
    all_paths = []
    for dir_path in dir_paths:
        all_paths += list_files(dir_path, depth)
    outdated_paths = filter_by_mtime(all_paths, datetime_th)
    if dry:
        print('delete {} files:'.format(len(outdated_paths)))
        pprint(outdated_paths[:50])
    else:
        delete_paths(outdated_paths)
