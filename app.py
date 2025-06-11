from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator
from unidecode import unidecode

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        text = request.json['text']
        target_lang = request.json['target_lang']
        
        # Translate to target language
        translator = GoogleTranslator(source='en', target=target_lang)
        translated_text = translator.translate(text)
        
        # Get pronunciation/transliteration using Unidecode
        pronunciation = unidecode(translated_text)
        
        return jsonify({
            'success': True,
            'translated_text': translated_text,
            'pronunciation': pronunciation
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True) 