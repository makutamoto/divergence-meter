#!/usr/bin/env python3
import sys
from serial import Serial

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write("Please specify a device, a divergence and an address.\n")
        sys.exit(-1)

    all = False
    if sys.argv[2].isdecimal():
        address = int(sys.argv[2])
        if address < 0 or address >= 4:
            sys.stderr.write("The address must be in range 0-3.\n")
            sys.exit(-2)
    else:
        if sys.argv[2] == 'all':
            all = True
        else:
            sys.stderr.write("The address must be a number or 'all'.\n")
            sys.exit(-3)

    with Serial(sys.argv[1], 9600) as s:
        if all:
            for i in range(4):
                s.write(bytes([0xFA]))
                s.write(bytes([0xF0 | i]))
        else:
            s.write(bytes([0xFA]))
            s.write(bytes([0xF0 | address]))
