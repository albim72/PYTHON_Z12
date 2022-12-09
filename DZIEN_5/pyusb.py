#pip install pyusb

from usb import core
import usb.core
#find device
dev = usb.core.find(idVendor=0x1516, idProduct=0x8628)
#found?
if dev is None :
        raise ValueError('device not found')

#set the active config. with no args, the first config will be the active one

dev.set_configuration()

#get an end point instance
ep = usb.util.find_descriptor(
    dev.get_interface_altsetting(), #first interface
    #match the first Out Endpoint
    custom_match = \
        lambda e: \
            usb.util.endpoint_direction(e.bEndpointAddress) == \
            usb.util.ENDPOINT_OUT)
assert ep is not None

while(1):
    ep.write(0x5553424350DDBC880000000000000600000000000000000000000000000000)
    ep.write(0x5553425350ddbc880000000000)
