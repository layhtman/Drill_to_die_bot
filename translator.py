import requests, json

URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"
KEY = "trnsl.1.1.20200223T120147Z.363096b22c749225.d6ee33f40b5fef9a86aaf244e36dd696dd987078"

def translate_me(mytext):
    mytext = mytext.strip()
    params = {
        "key": KEY,     
        "text": mytext,
        "lang": 'en-ru'}
    if mytext == None or mytext == '' or mytext == ' ':
        mytext = 'Ошибка текста, попробуйте написать текст по другому'
        mytext = mytext.split(' ')
        return {'text': mytext}
    else:
        response = requests.get(URL ,params=params)
        return response.json()

def translate_me_rus(mytext):

    params = {
        "key": KEY,     
        "text": mytext,
        "lang": 'ru-en'}
    if mytext == None or mytext == '' or mytext == ' ':
        mytext = 'Ошибка текста, попробуйте написать текст по другому'
        mytext = mytext.split(' ')
        return {'text': mytext}
    else:
        response = requests.get(URL ,params=params)
        return response.json()