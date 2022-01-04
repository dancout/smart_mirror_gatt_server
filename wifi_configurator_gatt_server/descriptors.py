import dbus

from ble_gatt_server.service import Descriptor


# =================================================================================
# ==================================== CLASSES ====================================
# =================================================================================

# NOTE: EVERY DESCRIPTOR JUST HAS THE ONE ReadValue() FUNCTION

# =================================================================================
# ==================================== WIFI CONFIGURATOR STATE DESCRIPTOR =========
# =================================================================================

class wifi_cfg_state_Descriptor(Descriptor):
    """
    This class defines the Descriptor for the WiFi Configurator State.
    """

# ==================================== INIT DECLARATIONS ==========================

    # Define the UUID of this descriptor
    WIFI_CFG_STATE_DESCRIPTOR_UUID = "0001"

    # Define the initial value of this descriptor
    WIFI_CFG_STATE_DESCRIPTOR_VALUE = 0  # "IDLE"

    def __init__(self, characteristic):
        Descriptor.__init__(
            self, self.WIFI_CFG_STATE_DESCRIPTOR_UUID,
            ["read", "write"],
            characteristic)

# =================================================================================
# ==================================== HELPER FUNCTIONS ===========================
# =================================================================================

    def ReadValue(self, options):
        value = []
        desc = self.WIFI_CFG_STATE_DESCRIPTOR_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))

        return value


# =================================================================================
# ==================================== WIFI CONFIGURATOR SSID CHARACTERISTIC ======
# =================================================================================

class wifi_cfg_ssid_Descriptor(Descriptor):
    """
    This class defines the Descriptor for the WiFi Configurator SSID.
    """

# ==================================== INIT DECLARATIONS ==========================

    # Define the UUID of this descriptor
    WIFI_CFG_SSID_DESCRIPTOR_UUID = "0002"

    # Define the initial value of this descriptor
    WIFI_CFG_SSID_DESCRIPTOR_VALUE = ""  # blank

    def __init__(self, characteristic):
        Descriptor.__init__(
            self, self.WIFI_CFG_SSID_DESCRIPTOR_UUID,
            ["read"],
            characteristic)

# =================================================================================
# ==================================== HELPER FUNCTIONS ===========================
# =================================================================================

    def ReadValue(self, options):
        value = []
        desc = self.WIFI_CFG_SSID_DESCRIPTOR_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))

        return value


# =================================================================================
# ==================================== WIFI CONFIGURATOR PASSWORD CHARACTERISTIC ==
# =================================================================================

class wifi_cfg_pswd_Descriptor(Descriptor):
    """
    This class defines the Descriptor for the WiFi Configurator Password.
    """

# ==================================== INIT DECLARATIONS ==========================

    # Define the UUID of this descriptor
    WIFI_CFG_PSWD_DESCRIPTOR_UUID = "0003"

    # Define the initial value of this descriptor
    WIFI_CFG_PSWD_DESCRIPTOR_VALUE = ""  # blank

    def __init__(self, characteristic):
        Descriptor.__init__(
            self, self.WIFI_CFG_PSWD_DESCRIPTOR_UUID,
            ["read"],
            characteristic)

# =================================================================================
# ==================================== HELPER FUNCTIONS ===========================
# =================================================================================

    def ReadValue(self, options):
        value = []
        desc = self.WIFI_CFG_PSWD_DESCRIPTOR_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))

        return value


# =================================================================================
# =========================== WIFI CONFIGURATOR SECURITY MODE CHARACTERISTIC ======
# =================================================================================

class wifi_cfg_sec_Descriptor(Descriptor):
    """
    This class defines the Descriptor for the WiFi Configurator Security Mode.
    """

# ==================================== INIT DECLARATIONS ==========================

    # Define the UUID of this descriptor
    WIFI_CFG_SEC_DESCRIPTOR_UUID = "0004"

    # Define the initial value of this descriptor
    WIFI_CFG_SEC_DESCRIPTOR_VALUE = ""  # blank

    def __init__(self, characteristic):
        Descriptor.__init__(
            self, self.WIFI_CFG_SEC_DESCRIPTOR_UUID,
            ["read"],
            characteristic)

# =================================================================================
# ==================================== HELPER FUNCTIONS ===========================
# =================================================================================

    def ReadValue(self, options):
        value = []
        desc = self.WIFI_CFG_SEC_DESCRIPTOR_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))

        return value
