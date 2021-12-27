from ble_gatt_server.service import Service
from wifi_configurator_gatt_server.characteristics import (
    wifi_cfg_pswd, wifi_cfg_sec, wifi_cfg_ssid, wifi_cfg_state,)

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

    def __init__(self, index):
        self.security_mode = 2  # WPA2 (default)
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
        self.wifi_cfg_state = state

# ==================================== SSID =======================================

    def get_wifi_config_ssid(self):
        return self.wifi_cfg_ssid

    def set_wifi_config_ssid(self, ssid):
        self.wifi_cfg_ssid = ssid

# ==================================== PASSWORD ===================================

    def get_wifi_cfg_pswd(self):
        return self.wifi_cfg_pswd

    def set_wifi_config_pswd(self, pswd):
        self.wifi_cfg_pswd = pswd

# ==================================== SECURITY MODE ==============================

    def get_wifi_config_sec(self):
        return self.wifi_cfg_sec

    def set_wifi_config_sec(self, sec):
        self.wifi_cfg_sec = sec
