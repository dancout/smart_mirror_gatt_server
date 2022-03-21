#!/bin/bash

# TODO: May need to potentially sleep here so that the pi has a chance to "catch up" and realize
#       that it is actually connected to WiFi. We sometimes experience the case where the pi
#       restarts itself, but doesn't connect to WiFi within the first second of being on, so the
#       gatt server thinks the connection failed. So, a sleep of 1 or 2 seconds might be enough
#       to "catch up".
# Run the gatt server application
sudo python3 /home/pi/Documents/Projects/smart_mirror_gatt_server/main.py &

### Use unclutter to hide the mouse
unclutter -idle 0.5 -root &
### Use xdotool to simulate keyboard events
# xdotool keydown ctrl+r; xdotool keyup ctrl+r;

### These two lines of the script use sed to search through the Chromium preferences file and clear out any flags that would make the warning bar appear, a behavior you don’t really want happening on your Raspberry Pi Kiosk
sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences

STR=`python3 /home/pi/Documents/Projects/smart_mirror_gatt_server/scripts/get_if_connected_to_internet.py`
SUB='True'
if [[ "$STR" == *"$SUB"* ]];
then
#   Connected to the internet
  DISPLAY=:0.0 chromium-browser --noerrdialogs --disable-infobars --start-fullscreen https://smart-mirror-13618.web.app/\#/display-page/$DISPLAY_DEVICE_NAME &

else
#   Not connected to the internet
  DISPLAY=:0.0 chromium-browser --noerrdialogs --disable-infobars --incognito --start-fullscreen /home/pi/Documents/Projects/smart_mirror_gatt_server/browser_files/connecttowifi.html &
fi

# THIS FILE WILL HAVE TO BE RUN FROM THIS LOCATION:
# /etc/xdg/lxsession/LXDE-pi/autostart
