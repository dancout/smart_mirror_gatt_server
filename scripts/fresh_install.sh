#!/bin/bash

# Prompt user to enter their device name
echo "Enter the DISPLAY_DEVICE_NAME specified from the Firebase Document:"

# Take an input of what the device name will be and save as a variable
read DISPLAY_DEVICE_NAME

# Enter Documents
cd /home/pi/Documents

# create the Projects directory if it does not exist
PROJ="/home/pi/Documents/Projects/"
if [ ! -d "$PROJ" ]; then
  echo "Creating Projects directory"
  mkdir Projects
fi

# Enter Projects
cd Projects

# clone the project
git clone https://github.com/dancout/smart_mirror_gatt_server.git

# Check for any errors
if [[ $? > 0 ]]
then
    echo "Cloning git repo failed. Exiting."
    return 1
else
    echo "Successfully cloned repo"
fi

# Enter smart_mirror_gatt_server/scripts
cd smart_mirror_gatt_server/scripts

# run install dependencies
. install_dependencies.sh 

# Check for any errors
if [[ $? > 0 ]]
then
    echo "Installing dependencies failed. Exiting"
    return 1
else
    echo "Successfully installed dependencies"
fi

# run set display device name with input device variable
. set_display_device_name.sh $DISPLAY_DEVICE_NAME

# Check for any errors
if [[ $? > 0 ]]
then
    echo "Setting up device name failed. Exiting"
    return 1
else
    echo "Successfully set up device name"
fi

# Message user that setup has completed
echo "Setup complete!"
echo "Sleeping for 5 seconds before rebooting"

# Sleep for 5 seconds for the user to read the message
sleep 5

# finally, reboot the machine so that the changes take effect
sudo reboot