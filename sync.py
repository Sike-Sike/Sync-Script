from dirsync import sync
import os

src="/Path/to/source"
print("\nSource : "+src)
dest = "Path/to/destination"
print("Destination : "+dest+"\n")

if(os.path.exists(dest)):
    if(os.path.exists(src)):
        sync(src,dest,'diff')
        sync(src,dest,'sync',purge=True)
        print("Sync complete")
    else:
        print("Source directory does not exist. Aborting sync...")
else:
    print("Destination directory does not exitst. Aborting sync...")
