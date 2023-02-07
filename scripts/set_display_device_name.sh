#!/bin/bash

# NOTE: This function requires a single input that will represent the DISPLAY_DEVICE_NAME
#       for this smart mirror.

# Make the /etc/environment file editable
sudo chmod 777 /etc/environment

# Add the input DISPLAY_DEVICE_NAME
echo "DISPLAY_DEVICE_NAME=$1" > "/etc/environment"
source /etc/environment

# Make the /etc/environment file read-only
sudo chmod 444 /etc/environment

# Update the DISPLAY_DEVICE_NAME in the connecttowifi.html file
sed -i "s/{{DISPLAY_DEVICE_NAME}}/$DISPLAY_DEVICE_NAME/g" /home/pi/Documents/Projects/smart_mirror_gatt_server/browser_files/connecttowifi.html

# Update the DISPLAY_DEVICE_NAME in the ble_app.py file
sed -i "s/{{DISPLAY_DEVICE_NAME}}/$DISPLAY_DEVICE_NAME/g" /home/pi/Documents/Projects/smart_mirror_gatt_server/constants.py

# Create the machine-info file if it does not already exist
sudo touch /etc/machine-info

# Make the machine-info file editable
sudo chmod 777 /etc/machine-info

# Update the PRETTY_HOSTNAME in the /etc/machine-info file, used for BLE connection
sudo echo "PRETTY_HOSTNAME=IMP - $1" > "/etc/machine-info"

# Make the /machine-info file read-only
sudo chmod 444 /etc/machine-info