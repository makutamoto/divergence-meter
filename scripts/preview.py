#!/usr/bin/env python3
import sys
from serial import Serial

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write("Please specify a device and divergence.\n")
        sys.exit(-1)

    if len(sys.argv[2]) != 8:
        sys.stderr.write("The divergence must have 8 digits.\n")
        sys.exit(-2)

    digits = []
    for char in sys.argv[2]:
        if char == '.':
            digits.append(0x50)
        elif char.isdigit():
            digits.append(int(char))
        else:
            sys.stderr.write("Please enter a number as a divergence.\n")
            sys.exit(-3)

    with Serial(sys.argv[1], 9600) as s:
        s.write(bytes([0xFA]))
        for i, value in enumerate(digits):
            s.write(bytes([0x80 | i]))
            s.write(bytes([0xA0 | value >> 4 & 0x0F]))
            s.write(bytes([0xB0 | value & 0x0F]))
        s.write(bytes([0xC0]))
