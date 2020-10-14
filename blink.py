import sys
import time
import mido

from pymata4 import pymata4

"""
Setup a pin for digital output and a MIDI port for input.
Note on messages turn on the pin, likewise for note offs.
Each Arduino pin to be used is assigned to a particular
MIDI note.
"""

"""
Set arduino pin numbers connected to valves, and the MIDI
notes which will connect to them through the virtual port
opened by MIDO
"""
DIGITAL_PINS = {60:6, # note 60 is MIDI for C3
                62:7,
                64:8,
                65:13}


def blink(my_board, pins):
    """
    This function will toggle a digital pin.
    :param my_board: an PymataExpress instance
    :param pins: dictionary mapping MIDI notes to pins
    """

    # set the pin mode
    for (note,pin) in pins.items():
        my_board.set_pin_mode_digital_output(pin)

    # open a MIDI port and control the LED
    clio_port = mido.open_input('Clio', virtual=True)
    while True:
        message = clio_port.receive()
        m_type = message.type
        # if message is not a note on or note off type, ignore it
        if not m_type in ['note_on', 'note_off']:
            continue
        m_note = message.note
        # if message uses unassigned note, ignore it
        try:
            m_pin = pins[m_note]
        except KeyError:
            print("unassigned note: "+str(m_note))
            continue
        # send message to Arduino
        if m_type == 'note_on':
            my_board.digital_write(m_pin, 1)
        elif m_type == 'note_off':
            my_board.digital_write(m_pin, 0)
        else:
            pass



board = pymata4.Pymata4()
try:
    blink(board, DIGITAL_PINS)
except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)
