import dbus

from ble_gatt_server.service import Characteristic
from wifi_configurator_gatt_server.descriptors import (
    wifi_cfg_pswd_Descriptor, wifi_cfg_sec_Descriptor, wifi_cfg_ssid_Descriptor, wifi_cfg_state_Descriptor,)

# ==================================== GLOBAL DECLARATIONS ========================


# GATT Characteristic Interface
GATT_CHRC_IFACE = "org.bluez.GattCharacteristic1"

# The time, in miliseconds, for a timeout on a Notify call
NOTIFY_TIMEOUT = 5000

# =================================================================================
# ==================================== CLASSES ====================================
# =================================================================================

# =================================================================================
# ==================================== WIFI CONFIGURATOR STATE CHARACTERISTIC =====
# =================================================================================


class wifi_cfg_state(Characteristic):
    """
    This class defines the WiFi Configurator State Characteristic.
    """

# ==================================== INIT DECLARATIONS ==========================

    WIFI_CFG_STATE_UUID = "00000001-b070-45da-ae51-9bd02af63ff1"

    def __init__(self, service):

        # This Characteristic has the option to notify, but we want to default this
        # value to False initially.
        self.notifying = False

        Characteristic.__init__(
            self, self.WIFI_CFG_STATE_UUID,
            ["notify", "write", "read"], service)
        self.add_descriptor(wifi_cfg_state_Descriptor(self))

# =================================================================================
# ==================================== HELPER FUNCTIONS ===========================
# =================================================================================

    def WriteValue(self, value, options):
        print('WiFI Configurator State Value received: ',
              (str(value)), flush=True)

        # Wrap this action in a try/except block in the case of an unexpected issue
        try:
            # decode the incoming value
            val = "".join(map(chr, value))
            print('Decoded State Value received: ', val, flush=True)
            # Set the internal wifi_config_state with the decoded val
            self.service.set_wifi_config_state(val)
        except Exception as e:
            print('There was an issue:', flush=True)
            print(str(e), flush=True)

        # Now that we are writing a new value to the WiFi Configurator State, we should notify any
        # listeners that a change has taken place!
        notifyValue = self.service.get_characteristics()[0].StartNotify()

        # Return the encoded value found from StartNotify()
        return notifyValue

    def get_wifi_cfg(self):
        # Define an empty list to store our decoded data value(s)
        value = []

        # Grab the state value from the internal storage
        state = self.service.get_wifi_cfg_state()

        # Print the current state we are sending out
        print('Sending State Value: ', state, flush=True)

        # Encode the data to be transferred via BLE
        for c in str(state):
            value.append(dbus.Byte(c.encode()))

        # Return the encoded data value
        return value

    def set_state_callback(self):
        if self.notifying:
            value = self.get_wifi_cfg()
            self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])

        return self.notifying

    def StartNotify(self):
        if self.notifying:
            return

        self.notifying = True
        print('Start notify WiFi Configurator Service', flush=True)

        value = self.get_wifi_cfg()
        self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])
        self.add_timeout(NOTIFY_TIMEOUT, self.set_state_callback)

        # Return the encoded value generated from get_wifi_cfg()
        return value

    def StopNotify(self):
        print('Stop notify WiFi Configurator Service', flush=True)
        self.notifying = False

    def ReadValue(self, options):
        print('State value Read Requested', flush=True)
        # Return the encoded wifi config state value
        return self.get_wifi_cfg()


# =================================================================================
# ==================================== WIFI CONFIGURATOR SSID CHARACTERISTIC ======
# =================================================================================

class wifi_cfg_ssid(Characteristic):
    """
    This class defines the WiFi Configurator SSID Characteristic.
    """

 # ==================================== INIT DECLARATIONS ==========================

    WIFI_CFG_SSID_UUID = "00000002-b070-45da-ae51-9bd02af63ff1"

    def __init__(self, service):

        Characteristic.__init__(
            self, self.WIFI_CFG_SSID_UUID,
            ["write"], service)
        self.add_descriptor(wifi_cfg_ssid_Descriptor(self))

# =================================================================================
# ==================================== HELPER FUNCTIONS ===========================
# =================================================================================

    def WriteValue(self, value, options):
        # TODO: Should we be printing this publicly?
        print('WiFI Configurator SSID Value received: ', (str(value)), flush=True)

        # TODO: Note: We deleted the "".join(map(chr, value)) code here, because it seemed excessive.
        #             It's possible it may be needed, only time will tell.
        self.service.set_wifi_config_ssid(value)

        # TODO: I believe that we should NOT be triggering a notify from this stage, as that will be handled
        #       when the state is set to "SAVING" (1) from the WIFI_CFG_STATE Characteristic.
        # self.service.get_characteristics()[0].StartNotify()


# =================================================================================
# ==================================== WIFI CONFIGURATOR PASSWORD CHARACTERISTIC ==
# =================================================================================

class wifi_cfg_pswd(Characteristic):
    """
    This class defines the WiFi Configurator Password Characteristic.
    """

# ==================================== INIT DECLARATIONS ==========================

    WIFI_CFG_PSWD_UUID = "00000003-b070-45da-ae51-9bd02af63ff1"

    def __init__(self, service):

        Characteristic.__init__(
            self, self.WIFI_CFG_PSWD_UUID,
            ["write"], service)
        self.add_descriptor(wifi_cfg_pswd_Descriptor(self))

# =================================================================================
# ==================================== HELPER FUNCTIONS ===========================
# =================================================================================

    def WriteValue(self, value, options):
        # TODO: Should we be printing this publicly?
        print('WiFI Configurator Password Value received: ',
              (str(value)), flush=True)

        # TODO: Note: We deleted the "".join(map(chr, value)) code here, because it seemed excessive.
        #             It's possible it may be needed, only time will tell.
        self.service.set_wifi_config_pswd(value)

        # TODO: I believe that we should NOT be triggering a notify from this stage, as that will be handled
        #       when the state is set to "SAVING" (1) from the WIFI_CFG_STATE Characteristic.
        # self.service.get_characteristics()[0].StartNotify()


# =================================================================================
# ============================= WIFI CONFIGURATOR SECURITY MODE CHARACTERISTIC ====
# =================================================================================

class wifi_cfg_sec(Characteristic):
    """
    This class defines the WiFi Configurator Security Mode Characteristic.
    """

# ==================================== INIT DECLARATIONS ==========================

    WIFI_CFG_SEC_UUID = "00000004-b070-45da-ae51-9bd02af63ff1"

    def __init__(self, service):

        Characteristic.__init__(
            self, self.WIFI_CFG_SEC_UUID,
            ["write"], service)
        self.add_descriptor(wifi_cfg_sec_Descriptor(self))

# =================================================================================
# ==================================== HELPER FUNCTIONS ===========================
# =================================================================================

    def WriteValue(self, value, options):
        # TODO: Should we be printing this publicly?
        print('WiFI Configurator Security Mode Value received: ',
              (str(value)), flush=True)

        # TODO: Note: We deleted the "".join(map(chr, value)) code here, because it seemed excessive.
        #             It's possible it may be needed, only time will tell.
        self.service.set_wifi_config_sec(value)

        # TODO: I believe that we should NOT be triggering a notify from this stage, as that will be handled
        #       when the state is set to "SAVING" (1) from the WIFI_CFG_STATE Characteristic.
        # self.service.get_characteristics()[0].StartNotify()
