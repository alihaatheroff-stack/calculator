from flask import Flask, request, jsonify
from calculator import add, subtract, multiply, divide, square_root, power

# Flask is a tiny web framework
# It lets our calculator receive web requests instead of keyboard input
app = Flask(__name__)

# This is the home page
# When someone visits your app URL they see this
@app.route('/')
def home():
    return '''
    <h1>🧮 Python Calculator</h1>
    <p>Use the API endpoints below:</p>
    <ul>
        <li>/add?a=5&b=3</li>
        <li>/subtract?a=5&b=3</li>
        <li>/multiply?a=5&b=3</li>
        <li>/divide?a=10&b=2</li>
        <li>/sqrt?a=9</li>
        <li>/power?a=2&b=8</li>
    </ul>
    '''

# Each route is one calculator operation
# ?a=5&b=3 means: first number is 5, second is 3
@app.route('/add')
def route_add():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = add(a, b)
    return jsonify({'operation': 'add', 'a': a, 'b': b, 'result': result})

@app.route('/subtract')
def route_subtract():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = subtract(a, b)
    return jsonify({'operation': 'subtract', 'a': a, 'b': b, 'result': result})

@app.route('/multiply')
def route_multiply():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = multiply(a, b)
    return jsonify({'operation': 'multiply', 'a': a, 'b': b, 'result': result})

@app.route('/divide')
def route_divide():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    try:
        result = divide(a, b)
        return jsonify({'operation': 'divide', 'a': a, 'b': b, 'result': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/sqrt')
def route_sqrt():
    a = float(request.args.get('a'))
    try:
        result = square_root(a)
        return jsonify({'operation': 'sqrt', 'a': a, 'result': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/power')
def route_power():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = power(a, b)
    return jsonify({'operation': 'power', 'a': a, 'b': b, 'result': result})

# Start the web server
# host='0.0.0.0' means accept connections from anywhere
# This is required for Render to reach your app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

