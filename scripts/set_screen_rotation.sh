#!/bin/bash


COMMAND_LINE_INPUT=$1

if [[ "$COMMAND_LINE_INPUT" == "" ]]
then
    # Prompt user to enter their desired screen rotation
    echo "Enter your desired screen rotation:"

    # Take in the rotation
    read SCREEN_ROTATION
else
    SCREEN_ROTATION="$COMMAND_LINE_INPUT"
fi

# Capitalize this variable
SCREEN_ROTATION=${SCREEN_ROTATION^^}

# Set a base balue for the screen rotation
CONVERTED_ROTATION_VALUE=0

if [[  "$SCREEN_ROTATION" == "DEFAULT" ]]
then
     CONVERTED_ROTATION_VALUE=0
elif [[ "$SCREEN_ROTATION" == "LEFT" ]]
then
     CONVERTED_ROTATION_VALUE=1
elif [[ "$SCREEN_ROTATION" == "UPSIDE_DOWN" ]]
then
     CONVERTED_ROTATION_VALUE=2
elif [[ "$SCREEN_ROTATION" == "RIGHT" ]]
then
     CONVERTED_ROTATION_VALUE=3  
else
    # No valid input was found
     echo "Please enter one of the following values: DEFAULT, LEFT, RIGHT, UPSIDE_DOWN"
     exit 1
fi

# Place the rotate value in the script
echo "#!/bin/bash" > /home/pi/Documents/Projects/smart_mirror_gatt_server/scripts/rotate_screen.sh
echo "" >> /home/pi/Documents/Projects/smart_mirror_gatt_server/scripts/rotate_screen.sh
# This sleep is absolutely necessary so that the command will be executed from the autostart file
echo "sleep 2" >> /home/pi/Documents/Projects/smart_mirror_gatt_server/scripts/rotate_screen.sh
echo "xrandr -o $CONVERTED_ROTATION_VALUE" >> /home/pi/Documents/Projects/smart_mirror_gatt_server/scripts/rotate_screen.sh
