#!/bin/bash

# Prompt user to enter their desired screen rotation
echo "Enter your desired screen rotation:"

# Take in the rotation
read SCREEN_ROTATION

# Capitalize this variable
SCREEN_ROTATION=${SCREEN_ROTATION^^}

CONVERTED_ROTATION_VALUE=0

if [[ "$SCREEN_ROTATION" == "NORMAL" ]]
then
    CONVERTED_ROTATION_VALUE=0

elif [[ "$SCREEN_ROTATION" == "LEFT" ]]
then
    CONVERTED_ROTATION_VALUE=1

elif [[ "$SCREEN_ROTATION" == "UPSIDE_DOWN"]]
then
    CONVERTED_ROTATION_VALUE=2

elif [[ "$SCREEN_ROTATION" == "RIGHT"]]
then
    CONVERTED_ROTATION_VALUE=3

else
then 
    echo "Please enter one of the following values: NORMAL, LEFT, RIGHT, UPSIDE_DOWN"
    return 1
fi

echo "xrandr -o {{CONVERTED_ROTATION_VALUE}} > "rotate_screen.sh"
