# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:22:27 2024

@author: Sepid
"""

import requests
import json

url = "http://127.0.0.1:8000/cardio_prediction"

test = {
        'age' : 36,
        'gender' : 1,
        'height' : 170,
        'weight' : 96.0,
        'ap_hi'  : 120,
        'ap_lo'  : 60,
        'cholesterol' : 3,
        'gluc' : 1,
        'smoke' : 0,
        'alco' : 0,
        'active' : 1,
        }

json_data = json.dumps(test)

response = requests.post(url,data=json_data)

print(response.text)