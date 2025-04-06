from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/game/<game_id>')
def game(game_id):
    return render_template('game.html', game_id=game_id)

@app.route('/games/balance-beam')
def balance_beam():
    return render_template('games/balance_beam.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
