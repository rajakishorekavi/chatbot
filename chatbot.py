# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:56:32 2020

@Description: To Run the Chatbot and get the responses.

@author: rajakishorekavi
"""

from wiki_api import *
from weather_api import *
from intent_entity_api import *
from env import *
from basic_msgs import *

import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm

from nltk.chat.util import Chat, reflections

def run_chatbot(msg):
    

    chat = Chat(pairs, reflections)

    rply = chat.respond(msg)
    
    if rply != None:
        return rply
    else:
 
        #model, vect = get_model_vect(model_file_name, vect_file_name)
        #msg_list = []
        #msg_list.append(msg)
        #trans_msg = vect.transform(msg_list)
        #intent = model.predict(trans_msg)
        
        intent = get_intent_luis(msg)
    
        #insert_msg_intent(msg, intent)
    
        if intent == 'weather' :

            doc = get_entity(msg)
            loc = ''

            for i in doc.ents:
                if i.label_ == 'GPE':
                    loc = i.text

            if loc == '' or loc == None:
                if msg.find('outside') != -1:
                    loc = get_location()

            weather_result = get_weather(loc)

            weather_reply = "Its "+str(weather_result['temp'])+" C with "+weather_result['description']+" in "+loc

            if msg.find("raining") != -1 :
                if weather_result['description'].find("rain") != -1:
                    weather_reply = "Yes! Its "+weather_result['description']+" with "+str(weather_result['temp'])+" C"
                else:
                    weather_reply = "No! Its not raining. Currently the temperature in "+loc+" is "+str(weather_result['temp'])+" C"


            return weather_reply

        elif intent == 'wikipedia' :

            return wiki(msg)
        
        elif intent == 'travel' :
            
            return "I'm still in Beta. This feature will be coming soon"
        
        else :
            
            return "I'm still in Beta. This feature will be coming soon"