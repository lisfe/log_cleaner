import log_cleaner

def main():
    from os import environ
    import datetime
    import json
    import pprint
    setting = {}
    dry_raw = environ.get('LOG_CLEANER_DRY', 'TRUE')
    if dry_raw == 'FALSE':
        setting['dry'] = False
    else:
        setting['dry'] = True
    log_dirs_raw = environ.get('LOG_CLEANER_DIRS','[]')
    setting['dir_paths'] = json.loads(log_dirs_raw)
    delta_day_raw = environ.get('LOG_CLEANER_DELTA_DAYS','7')
    setting['datetime_th'] = datetime.datetime.now() - datetime.timedelta(days=int(delta_day_raw))
    depth = int(environ.get('LOG_CLEANER_DEPTH', '1'))
    setting['depth'] = depth
    pprint.pprint(setting)

    log_cleaner.delete_outdated(**setting)

if __name__ == '__main__':
    main()