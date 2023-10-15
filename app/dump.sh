#!/bin/bash

# Database credentials
DB_USER="root"
DB_PASSWORD="root"
DB_NAME="ustora"

# Directory to store the backup (current directory of the script)
SCRIPT_DIR="$(dirname "${BASH_SOURCE[0]}")"
BACKUP_DIR="$SCRIPT_DIR"

rm -rf "$BACKUP_DIR/ustora_backup.sql"

# Dump the database to a SQL file
docker exec -i app-ustora_db-1 mysqldump -u$DB_USER -p$DB_PASSWORD $DB_NAME > "$BACKUP_DIR/ustora_backup.sql"

if [ $? -eq 0 ]; then
  echo "Database export completed successfully."
  echo "Backup saved as: $BACKUP_DIR/ustora_backup.sql"
else
  echo "Error: Database export failed."
fi
