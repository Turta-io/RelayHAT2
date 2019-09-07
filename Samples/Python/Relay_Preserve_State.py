#!/usr/bin/env python3

#This sample demonstrates state preserve functionality of the Relay HAT.
#Install Relay HAT 2 library with "pip3 install turta-relayhat2"

from time import sleep
from turta_relayhat2 import Turta_Relay

#Initialize
relay = Turta_Relay.RelayController(preserve_state = True)

#Read and increment the current relay state
state = relay.read_all() + 1
if (state == 32):
    state = 0

#Set the new relay state
relay.write_once(state)
print("Relay state is set")