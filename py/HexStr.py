#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 00:44:38 2025

@author: humayun404
"""

def hex_to_string(hex_str):
    # Remove '0x' prefix if present and any whitespace
    hex_str = hex_str.replace('0x', '').replace(' ', '').strip()
    
    # Validate hex string
    if not all(c in '0123456789ABCDEFabcdef' for c in hex_str):
        raise ValueError("Invalid hexadecimal string")
    
    try:
        # Convert hex to bytes then decode to string
        result = bytes.fromhex(hex_str).decode('utf-8')
        return result
    except UnicodeDecodeError:
        raise ValueError("Cannot decode hex string to valid UTF-8 string")
    except ValueError:
        raise ValueError("Invalid hexadecimal string format")

# Get input from user
try:
    hex_input = input("Enter a hexadecimal string: ")
    result = hex_to_string(hex_input)
    print("String:", result)
except ValueError as e:
    print("Error:", str(e))