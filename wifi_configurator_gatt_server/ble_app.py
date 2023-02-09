from ble_gatt_server.advertisement import Advertisement
from ble_gatt_server.service import Application
from constants.constants import DISPLAY_DEVICE_NAME

# This function houses the code for declaring the base BLE Application GAT Server.

# =================================================================================
# ==================================== CLASSES ====================================
# =================================================================================


# ==================================== BLE APPLICATION ============================

class BleApplication(Application):
    """
    This class defines the base BLE application object.
    """
    pass


# ==================================== ADVERTISEMENT ==============================

class SmartMirrorDisplayAdvertisement(Advertisement):
    """
    This class defines the Advertisement of the SmartMirrorDisplay device. It will give a localized
    name, and define itself as a peripheral device.
    """

    def __init__(self, index):
        Advertisement.__init__(self, index, "peripheral")
        # Declare this BLE Device name
        self.add_local_name(f"IMP - {DISPLAY_DEVICE_NAME}")
        self.include_tx_power = True
