from flask import Flask, render_template

from HP_funcoes import *

app = Flask(__name__, static_folder='assets', static_url_path='/assets')



@app.route('/')
def index():

    

    
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)