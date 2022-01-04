import os

# This file will house any utility functions used for the WiFi Configurator

# ======================================= Class Variables =====================================================================

# Represents the path to the wpa_supplicant.conf file
wpa_file_path = "/etc/wpa_supplicant/wpa_supplicant.conf"


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
