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
sed -i "s/{{DISPLAY_DEVICE_NAME}}/$DISPLAY_DEVICE_NAME/g" connecttowifi.html

# Make the /etc/environment file editable
sudo chmod 777 /etc/machine-info

# Update the PRETTY_HOSTNAME in the /etc/machine-info file, used for BLE connection
echo "PRETTY_HOSTNAME=IMP - $1" > "/etc/machine-info"

# Make the /etc/environment file read-only
sudo chmod 444 /etc/machine-info