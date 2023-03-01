from dirsync import sync
import os

src="/path/to/sourceDirectory"
print("\nSource : "+src)
dest = "path/to/destinationDirectory"
print("Destination : "+dest+"\n")

if(os.path.exists(src)):
    if(os.path.exists(dest)):
        sync(src,dest,'diff')
        print("Starting sync...")
        sync(src,dest,'sync',purge=True)
        print("Sync complete")
    else:
        print("Destination directory does not exist. Aborting sync...")
else:
    print("Source directory does not exitst. Aborting sync...")
