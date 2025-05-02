#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 00:43:05 2025

@author: humayun404
"""

def dec_to_hex(decimal):
    if decimal == 0:
        return "0"
    
    hex_digits = "0123456789ABCDEF"
    hex_result = ""
    
    # Convert decimal to hex
    while decimal > 0:
        remainder = decimal % 16
        hex_result = hex_digits[remainder] + hex_result
        decimal //= 16
    
    return hex_result

# Get input from user
try:
    decimal_num = int(input("Enter a decimal number: "))
    if decimal_num < 0:
        print("Please enter a non-negative number.")
    else:
        result = dec_to_hex(decimal_num)
        print("Hexadecimal:", result)
except ValueError:
    print("Please enter a valid integer.")