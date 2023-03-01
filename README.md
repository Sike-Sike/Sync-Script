# Sync-Script

This script used to  sync the contents of one directory to another.

To run the script, there are two options : 

Method 1

Method 2(Does not work well with git repositories)

---
- Method 1(rsync)

Replace ``path/to/sourceDirectory`` and ``path/to/destinationDirectory`` in rSync.sh by the appropriate paths to source and destination.

Give execute permission to rSync.sh by:
```    
    chmod +x ./rSync.sh
```

Finally run the script by:
```
    ./rSync.sh
```

- Method 2(python-dirsync)

Create a python environment which contains all the dependencies in requirements.txt.

Replace the ``path/to/python/environment`` by appropriate path to the python environment that was created in sync.sh.

Replace the ``path/to/sync.py`` by the actual path to sync.py in sync.sh.

Replace ``path/to/sourceDirectory`` and ``path/to/destinationDirectory`` in sync.py by the appropriate paths to source and destination.

Give execute permission to sync.sh by:
```    
    chmod +x ./sync.sh
```

Finally run the script by:
```
    ./sync.sh
```
