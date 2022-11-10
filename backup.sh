#!/bin/bash
 
# The source path to backup. Can be local or remote.
SOURCE=/home/alvaro/Desktop/Seguridad/
# Where to store the incremental backups
BACKUPDIR=/var/tmp/Backups
 
# Where to store today's backup
DEST="$BACKUPDIR/$(date +%d-%m-%Y)"
# Where to find yesterday's backup
YESTERDAY="$BACKUPDIR/$(date -d yesterday +%d-%m-%Y)/"
 
# Use yesterday's backup as the incremental base if it exists
if [ -d "$YESTERDAY" ]
then
	OPTS="--link-dest $YESTERDAY"
fi
 
# Run the rsync
rsync -av $OPTS "$SOURCE" "$DEST"
