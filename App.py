from flask import Flask
from markupsafe import Markup
from flask import render_template

app = Flask(__name__,template_folder='template/')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/first.html')
def firsr():
    return render_template('first.html')
    

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8080)