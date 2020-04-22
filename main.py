# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:45:54 2020

@Description: Main executable file. Run this file to run the application

@author: rajakishorekavi
"""

from wiki_api import *
from weather_api import *
from chatbot import *
from intent_entity_api import *
from env import *


import pandas as pd
import numpy as np
import pickle
import re
import requests, json 

import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm

from nltk.chat.util import Chat, reflections

import wikipedia

from flask import Flask, request
from flask import render_template
from flask import jsonify

app = Flask(__name__)
msg = []

@app.route('/')
def hello():
    #msg.append("Hi, I'm chatbot. Ask me anything.")
    return render_template(HOME_PAGE_FILE, host_url=JAVASCRIPT_IP, port_num=ENV_PORT )

@app.route('/api/', methods=["POST"])
def main_interface():
    response = request.get_json()
    reply = run_chatbot(response['message'])
    response.update({'reply': reply})
    return jsonify(response)

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response
