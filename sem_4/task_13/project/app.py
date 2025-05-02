from flask import Flask, render_template, request, send_file
from transformers import MarianMTModel, MarianTokenizer
from gtts import gTTS

def translate_text(text, src_lang, tgt_lang):
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs, use_cache=True)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text

def text_to_speech(text, lang_code, output_path="output.mp3"):
    tts = gTTS(text=text, lang=lang_code)
    tts.save(output_path)
    return output_path

app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['text']
        src_lang = request.form['src_lang']
        tgt_lang = request.form['tgt_lang']

        translated_text = translate_text(input_text, src_lang, tgt_lang)
        audio_file = text_to_speech(translated_text, tgt_lang)

        return render_template('index.html', translated=translated_text, audio_file=audio_file)

    return render_template('index.html')

@app.route('/audio')
def audio():
    return send_file("output.mp3", mimetype="audio/mpeg")

if __name__ == '__main__':
    app.run(debug=True)