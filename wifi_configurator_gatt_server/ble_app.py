from ble_gatt_server.advertisement import Advertisement
from ble_gatt_server.service import Application


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
        self.add_local_name("IMP - RaspberyPiDisplay")
        self.include_tx_power = True
