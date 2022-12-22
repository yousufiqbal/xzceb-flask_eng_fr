""" This module contains translator instance and translation functions """

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

# Loading envs..
load_dotenv()

# Setting apikey and url..
apikey = os.environ['apikey']
url = os.environ['url']

# Creating instance of 'IBM Watson Languate Translator'..
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text = None):
    """Function for english to french translation.."""

    # If no value is provided return None..
    if (english_text == None):
      return None

    # Else translate and return translation
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text = None):
    """Function for french to english translation.."""
    
    # If no value is provided return None..
    if (french_text == None):
      return None

    # Else translate and return translation
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
