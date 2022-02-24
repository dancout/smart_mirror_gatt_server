import os
from ble_gatt_server.service import Service
from wifi_configurator_gatt_server.characteristics import (
    wifi_cfg_pswd, wifi_cfg_sec, wifi_cfg_ssid, wifi_cfg_state,)
from wifi_configurator_gatt_server.utilities import update_wpa_file, update_state_file, get_state_from_file

# This file houses the Service Declarations for the BLE GATT Server.

# =================================================================================
# ==================================== CLASSES ====================================
# =================================================================================

# =================================================================================
# ==================================== WIFI CONFIGURATOR SERVICE ==================
# =================================================================================


class WiFiConfiguratorService(Service):
    """
    This class defines the WiFi Configurator Service. You will be able to set the SSID, Password,
    Security Mode, and WiFi state from here.
    """

# ==================================== INIT DECLARATIONS ==========================

    # The WiFi Configurator Service UUID
    WIFI_CONFIG_SVC_UUID = "00000000-b070-45da-ae51-9bd02af63ff1"

    # This represents the state where we need to begin joining to the WiFi.
    # This state will be set from the controller, and this GATT Server will be expected
    # to attempt to join the WiFi Network.
    JOIN_STATE = "3"

    # This represents the state signaling that it is time to attempt to join the WiFi
    # Network. This state will be set just before restarting the GATT Server.
    JOINING_STATE = "4"

    def __init__(self, index):
        # Set a default security mode and wifi config state
        self.security_mode = 2  # WPA2 (default)
        self.wifi_cfg_state = get_state_from_file()  # IDLE (default)
        Service.__init__(self, index, self.WIFI_CONFIG_SVC_UUID, True)
        self.add_characteristic(wifi_cfg_state(self))
        self.add_characteristic(wifi_cfg_ssid(self))
        self.add_characteristic(wifi_cfg_pswd(self))
        self.add_characteristic(wifi_cfg_sec(self))


# =================================================================================
# ==================================== HELPER FUNCTIONS ===========================
# =================================================================================

# ==================================== STATE ======================================

    def get_wifi_cfg_state(self):
        return self.wifi_cfg_state

    def set_wifi_config_state(self, state):
        """
        This function will set the WiFi Configuration state to the incoming [state]
        value. It will then update the state.txt file with this value. Finally, if
        the state was set to the "JOIN" status, it will update the wpa_supplicant.conf
        file with the current ssid & pswd, set the WiFi Configurator state to
        "JOINING", and then reboot the device.
        """
        # Set the incoming state on this Service object        
        self.wifi_cfg_state = state

        # Set the incoming state within the state.txt file
        update_state_file(state)

        # Check if state was "JOIN"
        if state == self.JOIN_STATE:
            # Update the wpa_supplicants.conf file with the current ssid & pswd
            update_wpa_file(self.get_wifi_config_ssid(), self.get_wifi_cfg_pswd())

            # Next, we'll need to set state to "JOINING"
            self.set_wifi_config_state(self.JOINING_STATE)

            # Then restart to apply the new WiFi Configuration
            os.system("sudo reboot")

# ==================================== SSID =======================================

    def get_wifi_config_ssid(self):
        return self.wifi_cfg_ssid

    def set_wifi_config_ssid(self, ssid):
        self.wifi_cfg_ssid = ssid

# ==================================== PASSWORD ===================================

    # TODO: THIS ISN'T NAMED CONSISTENTLY WITH THE OTHER 'config' vs 'cfg'!
    def get_wifi_cfg_pswd(self):
        return self.wifi_cfg_pswd

    def set_wifi_config_pswd(self, pswd):
        self.wifi_cfg_pswd = pswd

# ==================================== SECURITY MODE ==============================

    def get_wifi_config_sec(self):
        return self.wifi_cfg_sec

    def set_wifi_config_sec(self, sec):
        self.wifi_cfg_sec = sec
