from flask import Flask, request, jsonify
import requests
app = Flask(__name__)
@app.route('/check_login', methods=['GET'])
def check_login():
    username = request.args.get('username')
    password = request.args.get('password')
    
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
    
    url = 'https://b-api.facebook.com/method/auth.login'
    params = {
        'access_token': '237759909591655|0f140aabedfb65ac27a739ed1a2263b1',
        'format': 'json',
        'sdk_version': '2',
        'email': username,
        'locale': 'en_US',
        'password': password,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'
    }

    response = requests.get(url, params=params)
    result = response.json()
    cookies = response.cookies.get_dict()
    result['cookies'] = cookies
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
