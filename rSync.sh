#!/bin/bash

SRC=/path/to/sourceDirectory
DEST=/path/to/destinationDirectory

echo "Source : $SRC"
echo "Destination : $DEST"

if [[ -d $SRC ]] ; 
then
	if [[ -d $DEST ]] ;
	then
		echo "Starting sync..."
		rsync -av $SRC/ $DEST/
		echo "Sync Complete"
	else
		echo "Destination directory does not exist. Aborting sync..."
	fi
else
	echo "Source directory does not exist. Aborting sync..."
fi
