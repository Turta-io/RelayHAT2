#!/usr/bin/env python3

#This sample demonstrates toggling the relays.
#Install Relay HAT 2 library with "pip3 install turta-relayhat2"

from time import sleep
from turta_relayhat2 import Turta_Relay

#Initialize
relay = Turta_Relay.RelayController()

try:
    while 1:
        #Toggle relay 1
        relay.toggle(1)
        print("Toggle relay 1: " + ("On" if relay.read(1) else "Off"))
        sleep(2.0)

        #Toggle relay 2
        relay.toggle(2)
        print("Toggle relay 2: " + ("On" if relay.read(2) else "Off"))
        sleep(2.0)

        #Toggle relay 3
        relay.toggle(3)
        print("Toggle relay 3: " + ("On" if relay.read(3) else "Off"))
        sleep(2.0)

        #Toggle all relays
        relay.toggle_all()
        print("Toggle all relays: " + str(bin(relay.read_all())))
        sleep(2.0)

        #Toggle relay 4
        relay.toggle(4)
        print("Toggle relay 4: " + ("On" if relay.read(4) else "Off"))
        sleep(2.0)

        #Toggle relay 5
        relay.toggle(5)
        print("Toggle relay 5: " + ("On" if relay.read(5) else "Off"))
        sleep(2.0)

except KeyboardInterrupt:
    print('Bye.')
