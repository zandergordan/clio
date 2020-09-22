import sys
import time
import mido

from pymata4 import pymata4

"""
Setup a pin for digital output and a MIDI port for input.
Note on messages turn on the pin, likewise for note offs.
"""

# some globals
DIGITAL_PIN = 6  # arduino pin number


def blink(my_board, pin):
    """
    This function will toggle a digital pin.
    :param my_board: an PymataExpress instance
    :param pin: pin to be controlled
    """

    # set the pin mode
    my_board.set_pin_mode_digital_output(pin)

    # open a MIDI port and control the LED
    clio_port = mido.open_input('Clio', virtual=True)
    while True:
        message = clio_port.receive()
        print(message)
        if message.type == 'note_on':
            my_board.digital_write(pin, 1)
        elif message.type == 'note_off':
            my_board.digital_write(pin, 0)
        else:
            pass



board = pymata4.Pymata4()
try:
    blink(board, DIGITAL_PIN)
except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)
