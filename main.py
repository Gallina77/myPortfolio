from flask import session, redirect, url_for, request, render_template, Flask
from portfolio.morse_code_translator import MorseCodeTranslator
from portfolio.tic_tac_toe import TicTacToe
from portfolio.type_and_let_go import TypeAndLetGo
import os
import json
from transformers import pipeline
import torch


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')


#DATABASE_URL = os.environ.get('DB_URI')
#conn = psycopg2.connect(DATABASE_URL)
#Replace user and password with your Postgres username and password, host and #port with the values in your database URL, and database_name with the name of #your database.
#cur = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

#TODO: Fix the filtering
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/project_details/<project_id>')
def project_details(project_id):
    with open("./portfolio/project_details.json") as f:
        data = json.load(f)
        project = next((p for p in data["projects"] if p["id"] == project_id), None)

    return render_template('project_details.html', project=project)

#TODO: input validation and error handling
#TODO: when refreshing stay in the same area
#TODO: back-button
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

    return render_template('projects/morse_translator.html',
                           translated_text=translated_text,
                           input_text=input_text)

@app.route('/tic_tac_toe', methods=['GET', 'POST'])
def tic_tac_toe():
    # Handle reset with query param
    if request.method == 'GET' and request.args.get('reset_game'):
        # Clear session to reset the game
        session.pop('grid', None)
        session.pop('message', None)
        session.pop('game_over', None)
        return redirect(url_for('tic_tac_toe'))

    # Restore game state from session if it exists
    if 'grid' in session:
        game = TicTacToe()
        game.grid = session['grid']
        game.game_over = session.get('game_over', False)
        game.message = session.get('message')
    else:
        game = TicTacToe()

    # Handle player move on POST if game not over
    if request.method == 'POST' and not game.game_over:
        pos = request.form['cell']
        game.player_move(pos)
        if not game.game_over:
            game.ai_move()

        # Save updated state back to session
        session['grid'] = game.grid
        session['message'] = game.message
        session['game_over'] = game.game_over

        # Redirect after POST for clean refresh and avoid double POST on reload
        return redirect(url_for('tic_tac_toe'))

    return render_template('projects/tic_tac_toe.html',
                           board=game.grid,
                           message=game.message,
                           game_over=game.game_over)

@app.route('/type_and_let_go', methods=['GET', 'POST'])
def type_and_let_go():
    if request.method == 'GET' and request.args.get('new_prompt'):
        prompt = TypeAndLetGo().get_prompt()
    else:
        prompt = TypeAndLetGo().get_prompt()
    return render_template('projects/type_and_let_go.html', prompt=prompt)

@app.route('/writing')
def writing():
    prompt = request.args.get('prompt', '')
    return render_template('projects/writing.html', prompt=prompt, writing_time=100)


@app.route('/memory_palace')
def memory_palace():
    try:
        generator = pipeline('text-generation', model='gpt2')  # or distilgpt2 for a lighter version
        result = generator("What should I remember today?", max_length=50)
        return str(result)
    except Exception as e:
        return f"Error occurred: {e}", 500

if __name__ == '__main__':
    app.run(debug=False)