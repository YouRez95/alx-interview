#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

# True check
data = [467, 133, 108] 
print(validUTF8(data))


# True check
data = [240, 188, 128, 167]
print(validUTF8(data))


# False check
data = [345, 467]
print(validUTF8(data))


# True check
data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

# True check
data = [65]
print(validUTF8(data))

# False check
data = [229, 65, 127, 256]
print(validUTF8(data))