# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 02:41:15 2021

@author: Vitamin-C
"""

from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name.strip() == country_name.strip():
            return code
    # cover the case that no name is found
    return None

        
