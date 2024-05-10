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
    num_bytes = 0
    is_valid = True

    for element in data:
        binary = bin(element)[2:]
        if len(binary) <= 8:
            binary = '0' * (8 - len(binary)) + binary
        else:
            binary = binary[-8:]
        binary_data.append(binary)

    for j in range(len(binary_data)):
        for k in binary_data[j:j + num_bytes]:
            if k[0] != '1' or k[1] != '0':
                is_valid = False
                break
            else:
                continue

        if is_valid is False:
            break

        if j + num_bytes < len(binary_data):
            j = j + num_bytes
            num_bytes = 0
        else:
            break

        if binary_data[j].startswith("0"):
            continue
        elif binary_data[j].startswith("110"):
            if j == len(binary_data) - 1:
                is_valid = False
                break
            num_bytes = 1
            continue
        elif binary_data[j].startswith("1110"):
            if j == len(binary_data) - 1:
                is_valid = False
                break
            num_bytes = 2
            continue
        elif binary_data[j].startswith("11110"):
            if j == len(binary_data) - 1:
                is_valid = False
                break
            num_bytes = 3
            continue
        else:
            is_valid = False
            break
    return is_valid
