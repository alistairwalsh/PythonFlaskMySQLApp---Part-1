from flask import Flask, render_template, json, request

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(port=5002)