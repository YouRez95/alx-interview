#!/usr/bin/python3
"""
    validate the UTF-8
"""

from typing import List


def validUTF8(data: List) -> bool:
    '''
        method that determines if a given data set
        represents a valid UTF-8 encoding
    '''
    binary_data = []
    is_valid = True
    for num in data:
        binary = bin(num)[2:]
        if len(binary) < 8:
            binary = '0' * (8 - len(binary)) + binary
        elif len(binary) > 8:
            binary = binary[-8:]
        binary_data.append(binary)

    i = 0
    while i < len(binary_data):
        num_bytes = 0
        byte = binary_data[i]
        if byte.startswith('0'):
            num_bytes = 1
        elif byte.startswith('110'):
            num_bytes = 2
        elif byte.startswith('1110'):
            num_bytes = 3
        elif byte.startswith('11110'):
            num_bytes = 4
        else:
            is_valid = False
            break

        for j in range(i + 1, i + num_bytes):
            if j >= len(binary_data) or not binary_data[j].startswith('10'):
                is_valid = False
                break

        if is_valid is False:
            return is_valid
        i += num_bytes
    return is_valid
