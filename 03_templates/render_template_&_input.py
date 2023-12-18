from flask import *
app = Flask(__name__)

@app.route('/user/<name1>')
def home(name1):
    return render_template('with_input.html',name=name1)

if __name__=='__main__':
    app.run(debug= True)