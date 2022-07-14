from flask import Flask, redirect, render_template, url_for, request
import csv

app = Flask(__name__)
UPLOAD_FOLDER = '/static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

csv_rows = []

@app.route('/')
def hello_world():
    return 'Hello Wold'
@app.route('/hello/<name>')
def hello_world_name(name):
    return f'Hello Wold {name}'
    

@app.route('/cond/<name>')
def cond(name):
    if name == 'world':
        return redirect(url_for('hello_world'))
    else:
        return redirect(url_for(f'hello_world_name',name=name))


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        return render_template("success.html", name = f.filename)  

@app.route('/showpage')
def showpage():
    return render_template('hello.html')
if __name__ == '__main__':
    # app.run()
    app.run(debug=True)

