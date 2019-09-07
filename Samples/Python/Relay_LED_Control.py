#!/usr/bin/env python3

#This sample demonstrates turning relay indicator LEDs on and off.
#Install Relay HAT 2 library with "pip3 install turta-relayhat2"

from time import sleep
from turta_relayhat2 import Turta_Relay

#Initialize
relay = Turta_Relay.RelayController(leds_state = True)

try:
    while 1:
        #Toggle relays 1 to 5
        for x in range(1, 6):
            print("Toggling relay", x)
            relay.toggle(x)
            sleep(0.5)

        #Turn LEDs off
        print("Setting LEDs off")
        relay.set_leds(False)
        sleep(2.0)

        #Turn LEDs on
        print("Setting LEDs on")
        relay.set_leds(True)
        sleep(1.0)

        #Turn off all relays
        relay.write_all(False)
        print("Turn off all relays")
        sleep(1.0)

except KeyboardInterrupt:
    print('Bye.')