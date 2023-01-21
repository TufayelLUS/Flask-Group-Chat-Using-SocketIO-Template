from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('home.html')


@socketio.on('message')
def handle_message(message):
    # print('received message: ' + message)
    socketio.emit('message', message)

if __name__ == '__main__':
    socketio.run(app)
