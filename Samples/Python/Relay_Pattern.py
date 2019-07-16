#!/usr/bin/env python3

#This sample demonstrates controlling all the relays with one command.
#Install Relay HAT 2 library with "pip3 install turta-relayhat2"

from time import sleep
from turta_relayhat2 import Turta_Relay

#Initialize
relay = Turta_Relay.RelayController()

try:
    while 1:
        #Pattern 1
        relay.write_once(0b10101)
        print("Relay Pattern...: 10101")
        sleep(2.0)

        #Pattern 2
        relay.write_once(0b01010)
        print("Relay Pattern...: 01010")
        sleep(2.0)

        #Pattern 3
        relay.write_once(0b00100)
        print("Relay Pattern...: 00100")
        sleep(2.0)

except KeyboardInterrupt:
    print('Bye.')
