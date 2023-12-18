from flask import *
app = Flask(__name__)

@app.route('/table/<int:number>')
def table(number):
    return render_template('table_html.html',n = number)

if __name__=='__main__':
    app.run(debug=True)