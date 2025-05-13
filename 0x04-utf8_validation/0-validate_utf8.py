#!/usr/bin/python3
"""
UTF-8 Validation Module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
        data: List of integers where each integer represents 1 byte of data
        
    Returns:
        True if data is a valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # For each integer in the data array
    for num in data:
        # Get the 8 least significant bits (LSB) of the integer
        # as we're only concerned with the byte representation
        byte = num & 0xFF

        # If this is the start of a new UTF-8 character
        if n_bytes == 0:
            # Count how many bytes this character has by counting
            # the number of most significant bits set to 1
            if (byte >> 7) == 0:  # 0xxxxxxx (1 byte)
                n_bytes = 0
            elif (byte >> 5) == 0b110:  # 110xxxxx (2 bytes)
                n_bytes = 1
            elif (byte >> 4) == 0b1110:  # 1110xxxx (3 bytes)
                n_bytes = 2
            elif (byte >> 3) == 0b11110:  # 11110xxx (4 bytes)
                n_bytes = 3
            else:  # Invalid UTF-8 start byte
                return False
        else:
            # Check if the byte is a continuation byte (starts with 10)
            if (byte >> 6) != 0b10:
                return False
            # Decrement the number of bytes left in the current character
            n_bytes -= 1

    # If we've processed all bytes and we're not in the middle of a character
    return n_bytes == 0