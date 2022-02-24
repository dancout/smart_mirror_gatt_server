import os

# This file will house any utility functions used for the WiFi Configurator

# ======================================= Class Variables =====================================================================

# Represents the path to the wpa_supplicant.conf file
wpa_file_path = "/etc/wpa_supplicant/wpa_supplicant.conf"

# Represents the path to the state.txt file
state_file_path = "/home/pi/Documents/state.txt"


# ======================================= Class Functions =====================================================================


def update_wpa_file(ssid, pswd, country="US", key_mgmt="WPA-PSK"):
    """
    This function will overwrite the wpa_supplicant.conf file and add in the
    necessary WiFi information, based on the input [ssid] and [pswd], and
    optionally [country] or [key_mgmt].
    """
    # We MUST make this file writable, as by default it is read-only.
    os.system(f"sudo chmod 777 {wpa_file_path}")

    # Open the wpa_supplicant.conf file in "Overwrite" mode
    f = open(wpa_file_path, "w")

    # Overwrite the contents of the file with our new ssid and pswd
    f.write(f"""
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country={country}

network={{
        ssid="{ssid}"
        psk="{pswd}"
        key_mgmt={key_mgmt}
}}
    """)

    # Close the file
    f.close()

    # Print a success message.
    print(f"ssid and pswd written to {wpa_file_path}")

    # After editing, we should change the file back to read-only
    os.system(f"sudo chmod 444 {wpa_file_path}")


def update_state_file(state):
    """
    This function will write the incoming [state] to the proper state.txt
    file, located in the Documents folder. This represents the last set
    state of the Configurator. It will be used to retain state when the pi
    must restart to connect to WiFi, whereas any internal app state would
    be lost.
    """
    # Open the state.txt file in "Overwrite" mode
    f = open(state_file_path, "w")

    # Overwrite the contents of the file with our new state
    f.write(f"""{state}
    """)

    # Close the file
    f.close()

    # Print a success message.
    print(f"state saved to {state_file_path}")


def connected_to_internet():
    """
    This function will return true or false whether there is currently
    an internet connection or not.
    """

    # This represents the terminal command that will ping google.com to seek
    # a response
    ping = "ping -c2 google.com"

    # Store output of the ping
    output = os.popen(ping).read()

    # Define a String that should only be present if connected to the internet
    ping_success = "--- google.com ping statistics ---"

    # Check if the success String is present in the output
    if ping_success in output:
        print("Connected to internet.")
        return True
    # Else, there is no internet connection
    else:
        print("Not connected to internet.")
        return False


def get_state_from_file():
    """
    This function will return the state value listed from the file
    located at the variable [state_file_path].
    """

    # Set a default value of "IDLE" for state. This will be returned
    # if the state file does not yet exist.
    state = "0"

    # Check if the state file exists
    if os.path.exists(state_file_path):
        # Open the state.txt file in "Read" mode
        f = open(state_file_path)

        # Grab the first character found in this file
        state = f.read(1)

    # Return the current state
    return state


def check_if_joining():
    """
    This function will return true if the state found is "JOINING",
    (numerically this is "4"). Otherwise, it will return false.

    """
    # Get the current state
    state = get_state_from_file()

    # Return whether this state was "4" (meaning "JOINING" state) or not
    return state == "4"
