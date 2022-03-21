import sys
# The below will allow this file to import functions from parallel directories
sys.path.insert(0, '/home/pi/Documents/Projects/smart_mirror_gatt_server')

from wifi_configurator_gatt_server.utilities import connected_to_internet

print(connected_to_internet())