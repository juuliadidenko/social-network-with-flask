import json
import requests
from flask import current_app
from flask_babel import _


URL = "https://translate.api.cloud.yandex.net/translate/v2/translate"


def translate(text, source_lang, dest_lang):
    if 'TRANSLATOR_KEY' not in current_app.config or \
        not current_app.config['TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured')
    headers = {
        "Authorization": f"Api-Key {current_app.config['TRANSLATOR_KEY']}",
    }

    r = requests.post(
        URL,
        json={
            "sourceLanguageCode": source_lang,
            "targetLanguageCode": dest_lang,
            "format": "PLAIN_TEXT",
            "texts": text,
        },
        headers=headers)

    if r.status_code != 200:
        return _('Error: the translation service failed.')
    result =json.loads(r.content.decode('utf-8-sig'))
    return result["translations"][0]["text"]
