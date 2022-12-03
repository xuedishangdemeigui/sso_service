from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
CORS(app, resources=r'/*')


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    print(request.remote_addr)
    print(request.remote_user)
    print(request.user_agent)
    return jsonify(code=0, message="", data="hello world!")


@app.route('/html/login/')
def html_login(name=None):
    return render_template('login.html')
