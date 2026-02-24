from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "ash": "1234",
    "admin": "admin123"
}

@app.route('/')
def home():
    return jsonify({"message": "Login Service Running"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if users.get(username) == password:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "fail"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)