#!/bin/bash

# Run daily maintenance script
sudo periodic daily

# Run weekly maintenance script
sudo periodic weekly

# Run monthly maintenance script
sudo periodic monthly

# Clear inactive memory
sudo purge

# Check and repair file system
sudo fsck -fy

# Enable TRIM support for third-party SSDs
sudo trimforce enable

echo "All maintenance scripts completed."
