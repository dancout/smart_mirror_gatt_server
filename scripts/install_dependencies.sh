#!/bin/bash

# Update the system
sudo apt-get update -y
sudo apt-get dist-upgrade -y

# Check for any errors
if [[ $? > 0 ]]
then
    echo "Updating packages failed. Exiting"
    return 1
else
    echo "Successfully updated packages"
fi

# Install UPower to avoid multiple errors when opening the Chrome Browser
# from the command line.
sudo apt-get install -y upower

# Check for any errors
if [[ $? > 0 ]]
then
    echo "Installing upower failed. Exiting"
    return 1
else
    echo "Successfully installed upower"
fi

# Install unclutter to hide the mouse cursor
sudo apt-get install -y unclutter

# Check for any errors
if [[ $? > 0 ]]
then
    echo "Installing unclutter failed. Exiting"
    return 1
else
    echo "Successfully installed unclutter"
fi

# Update the autostart file so that the display never goes to sleep
# Make the autostart file editable
sudo chmod 777 /etc/xdg/lxsession/LXDE-pi/autostart

# Add a newline
echo "" >> /etc/xdg/lxsession/LXDE-pi/autostart

# Add lines to disable screensaver & power management, then call the bash script to run our Smart Mirror Display
echo "# Set the current xsession not to blank out the screensaver and then disables the screensaver altogether.
@xset s noblank
@xset s off
# disables the display power management system
@xset -dpms

# calls the script to open chrome to the correct address and run our gett server
@bash /home/pi/Documents/Projects/smart_mirror_gatt_server/scripts/run_smart_mirror_display.sh" >> /etc/xdg/lxsession/LXDE-pi/autostart

# Make the autostart file read-only
sudo chmod 444 /etc/xdg/lxsession/LXDE-pi/autostart
