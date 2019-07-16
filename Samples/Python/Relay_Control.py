#!/usr/bin/env python3

#This sample demonstrates turning relays on and off.
#Install Relay HAT 2 library with "pip3 install turta-relayhat2"

from time import sleep
from turta_relayhat2 import Turta_Relay

#Initialize
relay = Turta_Relay.RelayController()

try:
    while 1:
        #Turn on relay 1
        relay.write(1, True)
        print("Relay 1 state: " + ("On" if relay.read(1) else "Off"))
        sleep(1.0)

        #Turn on relay 2
        relay.write(2, True)
        print("Relay 2 state: " + ("On" if relay.read(2) else "Off"))
        sleep(1.0)

        #Turn on relay 3
        relay.write(3, True)
        print("Relay 3 state: " + ("On" if relay.read(3) else "Off"))
        sleep(1.0)

        #Turn on relay 4
        relay.write(4, True)
        print("Relay 4 state: " + ("On" if relay.read(4) else "Off"))
        sleep(1.0)

        #Turn on relay 5
        relay.write(5, True)
        print("Relay 5 state: " + ("On" if relay.read(5) else "Off"))
        sleep(1.0)

        #Turn off relay 1
        relay.write(1, False)
        print("Relay 1 state: " + ("On" if relay.read(1) else "Off"))
        sleep(1.0)

        #Turn off relay 2
        relay.write(2, False)
        print("Relay 2 state: " + ("On" if relay.read(2) else "Off"))
        sleep(1.0)

        #Turn off relay 3
        relay.write(3, False)
        print("Relay 3 state: " + ("On" if relay.read(3) else "Off"))
        sleep(1.0)

        #Turn off relay 4
        relay.write(4, False)
        print("Relay 4 state: " + ("On" if relay.read(4) else "Off"))
        sleep(1.0)

        #Turn off relay 5
        relay.write(5, False)
        print("Relay 5 state: " + ("On" if relay.read(5) else "Off"))
        sleep(1.0)

        #Turn on all relays
        relay.write_all(True)
        print("Turn on all relays")
        sleep(1.0)

        #Turn off all relays
        relay.write_all(False)
        print("Turn off all relays")
        sleep(1.0)

except KeyboardInterrupt:
    print('Bye.')