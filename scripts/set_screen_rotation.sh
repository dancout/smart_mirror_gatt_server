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

if [[  "$SCREEN_ROTATION" == "NORMAL" ]]
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
     echo "Please enter one of the following values: NORMAL, LEFT, RIGHT, UPSIDE_DOWN"
     exit 1
fi

# Place the rotate value in the script
echo "xrandr -o $CONVERTED_ROTATION_VALUE" > "rotate_screen.sh"
