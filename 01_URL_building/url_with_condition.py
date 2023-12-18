from flask import Flask,url_for,request,redirect
app = Flask(__name__)

@app.route('/admin')
def admin():
    return 'this is a admin pag where you can learn somany things'

@app.route('/librarion')
def librarion():
    return 'this is library page'

@app.route('/student')
def student():
    return 'this is the student portal'

@app.route('/user/<name>')
def user(name):
    if name=='admin':
        return redirect(url_for('admin'))
    elif name== 'librarion':
        return redirect(url_for('librarion'))
    else:
        return redirect(url_for('student'))

if __name__=='__main__':
    app.run(debug=True)