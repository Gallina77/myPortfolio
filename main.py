from flask import Flask, render_template, request
from sqlalchemy.orm import DeclarativeBase
from portfolio.morse_code_translator import MorseCodeTranslator
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
db = SQLAlchemy(model_class=Base)
db.init_app(app)

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