from flask import Flask, render_template

SCRIPT_NAME = '/humon'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
@app.route('/humon')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444)
