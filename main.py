# imports
from wifi_configurator_gatt_server.ble_app import BleApplication, SmartMirrorDisplayAdvertisement
from wifi_configurator_gatt_server.services import WiFiConfiguratorService


# =================================================================================
# ==================================== MAIN PROCESS ===============================
# =================================================================================


# ==================================== GLOBAL DECLARATIONS ========================

WIFI_CONFIGURATOR_SERVICE_INDEX = 0
SMART_MIRROR_ADVERTISEMENT_INDEX = 0

# ==================================== INIT DECLARATIONS ==========================

# Declare BLE Application
ble_app = BleApplication()

# Add the WiFi Configurator Service
ble_app.add_service(WiFiConfiguratorService(WIFI_CONFIGURATOR_SERVICE_INDEX))
ble_app.register()

# Add the SmartMirrorDisplay Advertisement
# This will make this device Bluetooth (BLE) Discoverable
ble_adv = SmartMirrorDisplayAdvertisement(SMART_MIRROR_ADVERTISEMENT_INDEX)
ble_adv.register()

# ==================================== RUN APPLICATION ============================

try:
    print('GATT application running')
    # TODO: IP Address might be nice to have, but not necessary for Proof of Concept.
    # fetchIpAddress()

    # Run the application
    ble_app.run()
except KeyboardInterrupt:
    # The user has used the keyboard to stop the application
    print('GATT closed by user')
    ble_app.quit()
    pass
except Exception as e:
    print(str(e))


# TODO: Below is how you can run terminal commands from a python file.
#       This could be useful when attempting to actually write to the wifi configuration
#       file and then reboot the pi.
#
#       os.system("sudo shutdown -h now")
