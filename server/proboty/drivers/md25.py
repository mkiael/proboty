# -*- coding: utf-8 -*-


try:
    from smbus import SMBus
except ImportError:
    from proboty.drivers.hwmocks.smbusmock import MockSMBus as SMBus


MD25_DEFAULT_ADDRESS = 0x58
MD25_DEFAULT_MODE = 0

MD25_REGISTER_SPEED1 =              0x00
MD25_REGISTER_SPEED2_TURN =         0x01
MD25_REGISTER_ENC1A =               0x02
MD25_REGISTER_ENC1B =               0x03
MD25_REGISTER_ENC1C =               0x04
MD25_REGISTER_ENC1D =               0x05
MD25_REGISTER_ENC2A =               0x06
MD25_REGISTER_ENC2B =               0x07
MD25_REGISTER_ENC2C =               0x08
MD25_REGISTER_ENC2D =               0x09
MD25_REGISTER_BATTERY_VOLTS =       0x0A
MD25_REGISTER_MOTOR1_CURRENT =      0x0B
MD25_REGISTER_MOTOR2_CURRENT =      0x0C
MD25_REGISTER_SOFTWARE_REV =        0x0D
MD25_REGISTER_ACCELERATION_RATE =   0x0E
MD25_REGISTER_MODE =                0x0F
MD25_REGISTER_COMMAND =             0x10


class Md25(object):
    """Handles communication with an Md25 board over I2C."""
    def __init__(self):
        self.address = MD25_DEFAULT_ADDRESS
        self.bus = SMBus(1)
        self.bus.write_byte_data(self.address, MD25_REGISTER_MODE, MD25_DEFAULT_MODE)

    def drive(self, speed_motor0, speed_motor1):
        self.bus.write_byte_data(self.address, MD25_REGISTER_SPEED1, speed_motor0)
        self.bus.write_byte_data(self.address, MD25_REGISTER_SPEED2_TURN, speed_motor1)
