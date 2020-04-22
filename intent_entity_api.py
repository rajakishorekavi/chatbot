# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:59:08 2020

@Description: Entity Extraction and Intent Prediction Module

@author: rajakishorekavi
"""

from env import *

import en_core_web_sm
import requests

def get_entity(msg):
    
    nlp = en_core_web_sm.load()
    
    doc = nlp(msg)
    return doc 

def get_intent_luis(msg):
    
    website = LUIS_WEB_API+msg
    
    r = requests.get(url = website) 
    data  = r.json()
    
    return data['topScoringIntent']['intent']
