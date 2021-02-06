from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def home_page():
    return render_template("home.html")



@app.route('/chat')
def hello():
    return render_template("chat.html")


if __name__ == '__main__':
    socketio.run(app, debug=True)