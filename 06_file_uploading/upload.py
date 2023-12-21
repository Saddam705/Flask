from flask import *
app =  Flask(__name__)

@app.route('/')
def upload():
    return render_template('file_upload.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
        res = request.files['file']
        res.save(res.filename)
        return  render_template('success.html',name=res.filename)

if __name__=='__main__':
    app.run(debug=True)