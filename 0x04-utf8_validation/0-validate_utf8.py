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
    for element in data:
        binary = bin(element)[2:]
        if len(binary) <= 8:
            for i in range(len(binary), 8):
                binary = '0' + binary
        else:
            binary = binary[-8:]
        binary_data.append(binary)

    num_bytes = 0
    is_valid = True
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

        if binary_data[j][0] == '0':
            continue
        elif (binary_data[j][0] == '1'
              and binary_data[j][1] == '1'
              and binary_data[j][2] == '0'):
            if j == len(binary_data) - 1:
                is_valid = False
                break
            num_bytes = 1
            continue
        elif (binary_data[j][0] == '1'
              and binary_data[j][1] == '1'
              and binary_data[j][2] == '1'
              and binary_data[j][2] == '0'):
            if j == len(binary_data) - 1:
                is_valid = False
                break
            num_bytes == 2
            continue
        else:
            is_valid = False
            break
    return is_valid
