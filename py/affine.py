#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  1 19:46:14 2025

@author: humayun404
"""

import math

plain = "BRIE"  
CT = "HDCQ"     

plain_nums = [ord(c) - ord('A') for c in plain]
ct_nums = [ord(c) - ord('A') for c in CT]

a_values = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

for a in a_values:
    for b in range(26):
        valid = True
        for p_num, c_num in zip(plain_nums, ct_nums):
            enc = (a * p_num + b) % 26
            if enc != c_num:
                valid = False
                break
        
        if valid:
            print("Found valid keys: a = " + str(a) + ", b = " + str(b))
