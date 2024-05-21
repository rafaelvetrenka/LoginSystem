from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    with open('login.txt', 'r') as login_file:
        valid_username = login_file.read().strip()
    
    with open('password.txt', 'r') as password_file:
        valid_password = password_file.read().strip()
    
    if username == valid_username and password == valid_password:
        return redirect('/success')
    else:
        return redirect('/blocked')

@app.route('/success')
def success():
    return render_template_string(open('success.html').read())

@app.route('/blocked')
def blocked():
    return render_template_string(open('blocked.html').read())

if __name__ == '__main__':
    app.run(debug=True)
