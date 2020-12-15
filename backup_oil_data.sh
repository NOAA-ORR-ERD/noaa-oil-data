#!/usr/bin/env bash
#
# Back up the current MongoDB oil database
#
# This is intended to be run from inside the oil database
# web_api Docker container.
#

echo "Current directory:" $(pwd)

oil_db_backup --config /config/config_oil_db.ini 

read -r uid gid <<<$(ls -ld ./data |awk '{print $3 " " $4}')

echo "User ID:" $uid ", Group ID:" $gid

chgrp -R $gid ./data
chown -R $uid ./data

