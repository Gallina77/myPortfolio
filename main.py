from flask import Flask, render_template, request, flash, redirect, url_for
from portfolio.morse_code_translator import MorseCodeTranslator


app = Flask(__name__)
app.secret_key = "Here is my secret key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/morse_translator', methods=['GET', 'POST'])
def morse_translator():
    # Initialize translator
    translator = MorseCodeTranslator()
    input_text = ""
    translated_text = ""
    if request.method == 'POST':
        mode = request.form.get('translation_mode')
        if mode == "text_to_morse":
            input_text = request.form['input_text']
            translated_text= translator.encrypt(input_text)
        elif mode == "morse_to_text":
            input_text = request.form['input_text']
            translated_text = translator.decrypt(input_text)

    return render_template('morse_translator.html',
                           translated_text=translated_text,
                           input_text=input_text)

if __name__ == '__main__':
    app.run(debug=False)