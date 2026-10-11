from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# 1. Basic Home Route
@app.route('/')
def home():
    return "Hello, this is our first Flask website!"

# 2. Routing with Dynamic String Variable
@app.route('/home/<name>')
def home_variable(name):
    return f"Hello, {name}!"

# 3. Routing with Type Converter (int)
@app.route('/home/<int:age>')
def display_age(age):
    return f"Age = {age}"

# 4. Dynamic URL Building & Redirection Example
@app.route('/admin')
def admin():
    return "Welcome to the Admin Dashboard"

@app.route('/student')
def student():
    return "Welcome to the Student Portal"

@app.route('/user/<name>')
def user_redirect(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    elif name == 'student':
        return redirect(url_for('student'))
    else:
        return f"User '{name}' not found."

# 5. Handling POST Method Form Submission
@app.route('/login', methods=['POST'])
def login_post():
    uname = request.form.get('uname')
    passwrd = request.form.get('pass')
    
    if uname == "ayush" and passwrd == "google":
        return f"Welcome {uname} (Logged in via POST)"
    else:
        return "Invalid Credentials", 401

# 6. Handling GET Method Form Submission
@app.route('/login-get', methods=['GET'])
def login_get():
    uname = request.args.get('uname')
    passwrd = request.args.get('pass')
    
    if uname == "ayush" and passwrd == "google":
        return f"Welcome {uname} (Logged in via GET)"
    else:
        return "Invalid Credentials", 401

if __name__ == '__main__':
    # Start local development server on port 5000
    app.run(host='127.0.0.1', port=5000, debug=True)