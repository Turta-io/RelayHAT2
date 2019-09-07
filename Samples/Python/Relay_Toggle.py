#!/usr/bin/env python3

#This sample demonstrates toggling the relays.
#Install Relay HAT 2 library with "pip3 install turta-relayhat2"

from time import sleep
from turta_relayhat2 import Turta_Relay

#Initialize
relay = Turta_Relay.RelayController()

try:
    while 1:
        #Toggle relays 1 to 5
        for x in range(1, 6):
            print("Toggling relay", x)
            relay.toggle(x)
            sleep(2.0)

        #Toggle all relays
        relay.toggle_all()
        print("Toggling all relays")
        sleep(2.0)

except KeyboardInterrupt:
    print('Bye.')
