#!/usr/bin/env python3
import sys
from serial import Serial

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write("Please specify a device.\n")
        sys.exit(-1)

    with Serial(sys.argv[1], 9600) as s:
        s.write(bytes([0xFA]))
        s.write(bytes([0x40]))
