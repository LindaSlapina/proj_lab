from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/kontaktinfo')
def kontaktinfo():
    return render_template('kontaktinfo.html')

@app.route('/pasutisana')
def pasutisana():
    return render_template('pasutisana.html')

if __name__ == '__main__':
    app.run(debug=True)
