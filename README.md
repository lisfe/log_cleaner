# Log Cleaner

load parameter from environment variable and delete outdated file.

## PARAMETER:

#### LOG_CLEANER_DRY
if LOG_CLEANER_DRY is set FALSE,
Log cleaner will really delete the outdated file in LOG_CLEANER_DIRS

#### LOG_CLEANER_DIRS
absolute dir paths in array in json format.
EX: ["/var/log/apache2","/var/log"]

#### LOG_CLEANER_DELTA_DAYS
define how many days is outdated.
if it is set 4, the file in LOG_CLEANER_DIRS and its mtime is small than (now - 4d) will be deleted.

#### LOG_CLEANER_DELTA_DEPTH
default is 1
expand how many level dir upder the path
all files in the tree will include and filter by mtime

## EXAMPLE:
```
LOG_CLEANER_DIRS='["/var/log/apache2"]' LOG_CLEANER_DELTA_DAYS='7' LOG_CLEANER_DRY=FALSE LOG_CLEANER_DEPTH=1 log-clean
```

### cron

```
3 3 * * * LOG_CLEANER_DIRS='["/var/log/apache2"]' LOG_CLEANER_DELTA_DAYS='7' LOG_CLEANER_DRY=FALSE LOG_CLEANER_DEPTH=2 /<path>/log-clean
```
