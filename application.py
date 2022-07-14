from flask import Flask, redirect, render_template, url_for, request
import csv

app = Flask(__name__)
UPLOAD_FOLDER = '/static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

csv_rows = []
filtered = []
with open('static/data-1.csv', 'r') as inFile:
    reader = csv.reader(inFile)
    csv_rows = [row for row in reader]
csv_rows.pop(0)
# print(csv_rows)


@app.route('/')
def hello_world():
    return '<h1>Rahul Annae - 1001979222</h1>'


@app.route('/11', methods=['POST', 'GET'])
def task11():
    if request.method == 'POST':
        print(request.form)
        range_from = int(request.form['range_from'])
        range_to = int(request.form['range_to'])
        return redirect(url_for('task11results',rangefrom=range_from, rangeto=range_to))
    else:
        return render_template('task11.html')


@app.route('/11results/<rangefrom>/<rangeto>')
def task11results(rangefrom,rangeto):
    filtered = list(filter(lambda item: int(item[1]) <= int(rangeto) and int(item[1]) >= int(rangefrom), csv_rows))
    print('filtered')
    print(filtered)
    return render_template('task11results.html', results=filtered)


@app.route('/10')
def task10():
    return render_template('hello.html')


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
