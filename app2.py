
from flask import Flask, render_template, json, request, g
import sqlite3

app = Flask(__name__)

DATABASE = '/database/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.route('/database')
def index():
    cur = get_db().cursor()


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        
if __name__ == "__main__":
    app.run(port=5002)        