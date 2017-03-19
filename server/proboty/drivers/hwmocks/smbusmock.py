# -*- coding: utf-8 -*-


class MockSMBus(object):
    """Mock class for the smbus module."""
    
    def __init__(self, bus_number):
        self.bus_number = bus_number

    def write_byte(self, addr, val):
        pass

    def write_byte_data(self, addr, cmd, val):
        pass
