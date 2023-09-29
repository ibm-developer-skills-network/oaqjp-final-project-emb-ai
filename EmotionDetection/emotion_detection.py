''' Module for Emotion Detection package '''

import requests

def emotion_detector(text_to_analyse):
    ''' Function to run emotion detection of user text input '''
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp\
    .v1/NlpService/EmotionPredict'
    header = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en\
    _stock'}
    myobj = {'raw_document': {'text': text_to_analyse}}
    response = requests.post(url, json = myobj, headers = header)
    return response.text
