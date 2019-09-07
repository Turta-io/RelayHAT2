# Turta Relay HAT 2 Helper for Raspbian.
# Distributed under the terms of the MIT license.

# Python Library for Serial Relay Controller.
# Version 1.0.1
# Released: July 16th, 2019
# Last Updated: September 7th, 2019

# Visit https://docs.turta.io for documentation.

import time
from smbus import SMBus

class RelayController:
    """Serial Relay Controller."""

    #I2C Slave Address
    I2C_ADDRESS = None

    #Registers
    MCP23008_IODIR   = 0x00
    MCP23008_IPOL    = 0x01
    MCP23008_GPINTEN = 0x02
    MCP23008_DEFVAL  = 0x03
    MCP23008_INTCON  = 0x04
    MCP23008_IOCON   = 0x05
    MCP23008_GPPU    = 0x06
    MCP23008_INTF    = 0x07
    MCP23008_INTCAP  = 0x08
    MCP23008_GPIO    = 0x09
    MCP23008_OLAT    = 0x0A
    LEDS_ON_MASK     = 0x80
    PIN_ON_MASK      = 0x01
    RELAYS_MASK      = 0x1F

    #Variables
    leds_on = True
    pres_st = False

    #I2C Config
    bus = SMBus(1)

    #I2C Communication

    def _write_register(self, reg_addr, data):
        """Writes data to the I2C device.

        Parameters:
        reg_addr (byte): Write register address
        data (byte): Data to be written to the device"""

        self.bus.write_i2c_block_data(self.I2C_ADDRESS, reg_addr, [ data & 0xFF ])

    def _read_register_1ubyte(self, reg_addr):
        """Reads data from the I2C device.

        Parameters:
        reg_addr (byte): Read register address

        Returns:
        byte: Response from the device"""

        buffer = self.bus.read_i2c_block_data(self.I2C_ADDRESS, reg_addr, 1)
        return buffer[0]

    #Initialization

    def __init__(self, addr = 0x20, leds_state = True, preserve_state = False):
        """Initiates the MCP23008 I/O Expander to control relays.

        Parameters:
        addr (byte): Device address, default is 0x20
        leds_state (bool): Indicator LEDs state, default is True
        preserve_state (bool): Save the relay state even if the application exits, default is False"""

        #Save the parameters to global variables.
        self.pres_st = preserve_state
        self.leds_on = leds_state

        #Device address check.
        if not 0x20 <= addr <= 0x27:
            raise TypeError("Device address must be between 0x20 and 0x27.")
        self.I2C_ADDRESS = addr

        if preserve_state:
            if self._check_init() is False:
                self._set_initial_settings()

        else:
            #Initialize the port expander.
            self._set_initial_settings()
        
        self.is_initialized = True

    #Configuration

    def _check_init(self):
        """Checks if the port expander is already initialized.
        
        Returns:
        bool: Init state (True of False)"""

        io_dir = self._read_register_1ubyte(self.MCP23008_IODIR)
        return True if io_dir == 0x00 else False

    def _set_initial_settings(self):
        """Writes the initial settings to the IO expander."""

        #Set I/O direction to output.
        self._write_register(self.MCP23008_IODIR, 0x00)

        #Set input polarity to same logic state mode.
        self._write_register(self.MCP23008_IPOL, 0x00)

        #Set interrupt on change pins to none.
        self._write_register(self.MCP23008_GPINTEN, 0x00)

        #Set default value register to 0x00.
        self._write_register(self.MCP23008_DEFVAL, 0x00)

        #Set interrupt control register to previous pin value mode.
        self._write_register(self.MCP23008_INTCON, 0x00)

        #Set configuration register.
        self._write_register(self.MCP23008_IOCON, 0x00)

        #Set GPIO pull-up resistor mode.
        self._write_register(self.MCP23008_GPPU, 0x00)

        #Set port register to logic-low.
        self._write_register(self.MCP23008_GPIO, 0x00)

        #Set output latch register to logic-low.
        self._write_register(self.MCP23008_OLAT, 0x00)
        return

    def set_leds(self, st):
        """Controls the indication LEDs.

        Parameters:
        st (bool): Indicator LEDs state (True or False)"""

        self.leds_on = st

        port = self._read_register_1ubyte(self.MCP23008_OLAT)
        if st:
            port |= (self.PIN_ON_MASK << 7)
        else:
            port &= ~(self.PIN_ON_MASK << 7)
        self._write_register(self.MCP23008_OLAT, port)
        return

    #Relay Write Methods

    def write(self, ch, st):
        """Controls the relay.

        Parameters:
        ch (byte): Relay channel (1 to 5)
        st (bool): Relay state (True or False)"""

        port = self._read_register_1ubyte(self.MCP23008_OLAT)
        if st:
            port |= (self.PIN_ON_MASK << ch-1)
        else:
            port &= ~(self.PIN_ON_MASK << ch-1)
        self._write_register(self.MCP23008_OLAT, port)
        return

    def write_once(self, st):
        """Controls all the relays.

        Parameters:
        st (byte): Relay states (0b00000 to 0b11111)"""

        st = st & self.RELAYS_MASK
        self._write_register(self.MCP23008_OLAT, st | self.LEDS_ON_MASK if self.leds_on else st)
        return

    def write_all(self, st):
        """Turns on or off all the relays.

        Parameters:
        st (bool): Relay states (True or False)"""

        state = 0x1F if st else 0x00
        self._write_register(self.MCP23008_OLAT, state | self.LEDS_ON_MASK if self.leds_on else state)
        return

    def toggle(self, ch):
        """Inverts the relay's state.

        Parameters:
        ch (byte): Relay channel (1 to 5)"""

        port = self._read_register_1ubyte(self.MCP23008_OLAT)
        port ^= self.PIN_ON_MASK << ch-1
        self._write_register(self.MCP23008_OLAT, port | self.LEDS_ON_MASK if self.leds_on else port)
        return

    def toggle_all(self):
        """Inverts all the relay states."""

        port = self._read_register_1ubyte(self.MCP23008_OLAT)
        port ^= 0x1F
        self._write_register(self.MCP23008_OLAT, port | self.LEDS_ON_MASK if self.leds_on else port)
        return

    #Relay Read Methods

    def read(self, ch):
        """Reads the relay state.

        Parameters:
        ch (byte): Relay channel (1 to 5)

        Returns:
        bool: Relay state (True of False)"""

        port = self._read_register_1ubyte(self.MCP23008_OLAT)
        return True if (port >> ch-1) & self.PIN_ON_MASK == self.PIN_ON_MASK else False

    def read_all(self):
        """Reads all the relay states.

        Returns:
        byte: Relay states (0b00000 to 0b11111)"""

        port = self._read_register_1ubyte(self.MCP23008_OLAT)
        return port & self.RELAYS_MASK

    #Disposal

    def __del__(self):
        """Releases the resources."""
        try:
            if self.is_initialized:
                if not self.pres_st:
                    self.write_all(False)
                del self.is_initialized
        except:
            pass
