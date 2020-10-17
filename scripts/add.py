#!/usr/bin/env python3
import sys
from serial import Serial

if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.stderr.write("Please specify a device, a divergence and an address.\n")
        sys.exit(-1)

    if sys.argv[2].isdecimal():
        address = int(sys.argv[2])
        if address < 0 or address >= 4:
            sys.stderr.write("The address must be in range 0-3.\n")
            sys.exit(-2)
    else:
        sys.stderr.write("The address must be a number.\n")
        sys.exit(-3)

    if len(sys.argv[3]) != 8:
        sys.stderr.write("The divergence must have 8 digits.\n")
        sys.exit(-4)

    digits = []
    for char in sys.argv[3]:
        if char == '.':
            digits.append(0x50)
        elif char.isdecimal():
            digits.append(int(char))
        else:
            sys.stderr.write("Please enter a number as a divergence.\n")
            sys.exit(-5)

    with Serial(sys.argv[1], 9600) as s:
        s.write(bytes([0xFA]))
        for i, value in enumerate(digits):
            s.write(bytes([0x80 | i]))
            s.write(bytes([0xA0 | value >> 4 & 0x0F]))
            s.write(bytes([0xB0 | value & 0x0F]))
        s.write(bytes([0xE0 | address]))
