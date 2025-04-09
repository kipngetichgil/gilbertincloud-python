from flask import Flask, request, render_template

app = Flask(__name__)
application = app  # For AWS Elastic Beanstalk compatibility

@app.route('/')
def home():
    return "Welcome to gilbertincloud-python!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':  # Simple check for demo
            return f"Welcome, {username}! You are logged in."
        else:
            return "Invalid credentials, try again."
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)