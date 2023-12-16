from flask import Flask,url_for,redirect
app = Flask(__name__)

@app.route('/home')
def home():
    return 'Welcome to home page'

@app.route('/guest/<guest>')
def guest_1(guest):
    return  'Hello %s dear guest' %guest

@app.route('/user/<name>')
def user1(name):
    if name=='saddam':
        return redirect(url_for('home'))
    else:
        return redirect(url_for('guest_1',guest=name))

if __name__=='__main__':
    app.run(debug=True)