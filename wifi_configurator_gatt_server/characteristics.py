import dbus
import os

from subprocess import Popen

from ble_gatt_server.service import Characteristic
from wifi_configurator_gatt_server.descriptors import (
    wifi_cfg_pswd_Descriptor, wifi_cfg_custom_Descriptor, wifi_cfg_sec_Descriptor, wifi_cfg_ssid_Descriptor, wifi_cfg_state_Descriptor,)
from wifi_configurator_gatt_server.utilities import update_wpa_file

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

    # This represents the state where we need to begin joining to the WiFi.
    # This state will be set from the controller, and this GATT Server will be expected
    # to attempt to join the WiFi Network.
    JOIN_STATE = "3"

    # This represents the state signaling that it is time to attempt to join the WiFi
    # Network. This state will be set just before restarting the GATT Server.
    JOINING_STATE = "4"

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
        """
        This function represents what is to be called on each set state
        callback. If notifying, it wll check if the state was set to the
        "JOIN" status, it will update the wpa_supplicant.conf file with
        the current ssid & pswd, set the WiFi Configurator state to
        "JOINING", and finally reboot the device.
        """
        if self.notifying:
            value = self.get_wifi_cfg()
            self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": value}, [])

            # Grab the state value from the internal storage
            state = self.service.get_wifi_cfg_state()

            # Next, we need to check if we are attempting to join the
            # WiFi Network. We are doing so in this callback function
            # because we need this code to be run separately from any
            # state setter function. The mobile controller is expecting
            # the setter function to return a success value, and if we
            # reboot this device then the success value is never sent
            # out.

            # Check if state was "JOIN"
            if state == self.JOIN_STATE:
                # Update the wpa_supplicants.conf file with the current ssid & pswd
                update_wpa_file(self.service.get_wifi_config_ssid(), self.service.get_wifi_cfg_pswd())

                # Next, we'll need to set state to "JOINING"
                self.service.set_wifi_config_state(self.JOINING_STATE)

                # Then restart to apply the new WiFi Configuration
                os.system("sudo reboot")

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

        # decode the incoming value
        val = "".join(map(chr, value))
        # TODO: Should we be printing this publicly?
        print('Decoded SSID Value received: ', val, flush=True)
        # Set the internal wifi_config_ssid with the decoded val
        self.service.set_wifi_config_ssid(val)


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

        # decode the incoming value
        val = "".join(map(chr, value))
        # TODO: Should we be printing this publicly?
        print('Decoded Password Value received: ', val, flush=True)
        # Set the internal wifi_config_pswd with the decoded val
        self.service.set_wifi_config_pswd(val)



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

        # decode the incoming value
        val = "".join(map(chr, value))
        # TODO: Should we be printing this publicly?
        print('Decoded Security Mode Value received: ', val, flush=True)
        # Set the internal wifi_config_pswd with the decoded val
        self.service.set_wifi_config_sec(val)


# =================================================================================
# ==================================== WIFI CONFIGURATOR CUSTOM CHARACTERISTIC ====
# =================================================================================

class wifi_cfg_custom(Characteristic):
    """
    This class defines the WiFi Configurator CUSTOM Characteristic.
    """

 # ==================================== INIT DECLARATIONS ==========================

    WIFI_CFG_CUSTOM_UUID = "00000005-b070-45da-ae51-9bd02af63ff1"

    def __init__(self, service):

        Characteristic.__init__(
            self, self.WIFI_CFG_CUSTOM_UUID,
            ["write"], service)
        self.add_descriptor(wifi_cfg_custom_Descriptor(self))

# =================================================================================
# ==================================== HELPER FUNCTIONS ===========================
# =================================================================================

    
    def WriteValue(self, value, options):
        print('WiFI Configurator CUSTOM Value received: ', (str(value)), flush=True)

        # decode the incoming value
        val = "".join(map(chr, value))
        print('Decoded CUSTOM Value received: ', val, flush=True)
        Popen(f"echo Sleeping before running command;sleep 5;echo Running command;{val}", shell=True,
                stdin=None, stdout=None, stderr=None,
        )

        # Set the internal wifi_config_custom with the decoded val
        self.service.set_wifi_config_custom(val)
