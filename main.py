import socket

from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__, static_folder="static")

def init_send_socket(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, int(port)))
    print('Send socket connected')

    return s

def init_receive_socket(ip, port):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((ip, int(port)))
    serversocket.listen(1)
    (clientsocket, address) = serversocket.accept()
    print('Receive socket connected')

    return clientsocket

def init_socket(func, ip, port):
    socket = ''
    try:
        while socket == '':
            socket = func(ip, port)
    except ConnectionRefusedError:
        print('Connection refused')
        socket = init_socket(func, ip, port)

    return socket

sockets = {}
messages = []

@app.route('/', methods=['GET'])
def mainn():
    return render_template('main.html')

@app.route('/chat', methods=['POST'])
def chat():
    if request.form.get('number') == '1':
        sockets['send'] = init_socket(init_send_socket, request.form.get('ip'), request.form.get('sport'))
        sockets['receive'] = init_socket(init_receive_socket, request.form.get('ip'), request.form.get('rport'))
    elif request.form.get('number') == '2':
        sockets['receive'] = init_socket(init_receive_socket, request.form.get('ip'), request.form.get('rport'))
        sockets['send'] = init_socket(init_send_socket, request.form.get('ip'), request.form.get('sport'))
    else:
        return 'error'

    return render_template('chat.html', json=messages)

@app.route('/json', methods=['GET'])
def json():
    return jsonify(messages)

@app.route('/receive', methods=['GET'])
def receive():
    try:
        data = sockets['receive'].recv(1024)
    except KeyError:
        return redirect('/chat1')
    if not data == b'':
        messages.append('2: ' + data.decode())

    return 'ok'

@app.route('/send', methods=['POST'])
def send():
    message = request.get_json(force=True)['message']
    sockets['send'].send(bytes(message, encoding = 'UTF-8'))
    messages.append('1: ' + message)

    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)
