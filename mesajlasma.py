from flask import Flask, request, render_template
import time

app = Flask(__name__)

message_history = {}

@app.route('/')
def hello():
    return render_template('/index.html')

def add_to_dict(key, value):
    if key not in message_history:
        message_history[key] = []
    message_history[key].append(value)

    
@app.route('/first_endpoint', methods=['POST'])
def first_endpoint():
    global message_history
    ip_address = request.remote_addr
    user_id = generate_user_id(ip_address)
    message = request.data.decode('utf-8')
    print('mustafa',str(user_id))
    if message:
        add_to_dict(str(time.time()), [str(user_id),message])

    return "Message received and recorded."

def generate_user_id(ip_address):
    # Basit bir user id üretmek için IP adresinden bir hash alabilirsiniz
    # Daha güvenli bir yöntem için özel bir kullanıcı kimliği üretme algoritması kullanabilirsiniz
    return hash(ip_address)

@app.route('/second_endpoint', methods=['GET'])
def second_endpoint():
    global message_history
    if message_history:
        return message_history
    else:
        return "No message history available."

@app.route('/whatismyuserid', methods=['GET'])
def whatismyuserid():
    ip_address = request.remote_addr
    user_id = generate_user_id(ip_address)
    return str(user_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
