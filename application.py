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
    return render_template('data.html', results=csv_rows)


@app.route('/11', methods=['POST', 'GET'])
def task11():
    if request.method == 'POST':
        print(request.form)
        range_from = int(request.form['range_from'])
        range_to = int(request.form['range_to'])
        return redirect(url_for('task11results', rangefrom=range_from, rangeto=range_to))
    else:
        return render_template('task11.html')


@app.route('/11results/<rangefrom>/<rangeto>')
def task11results(rangefrom, rangeto):
    filtered = list(filter(lambda item: int(item[1]) <= int(
        rangeto) and int(item[1]) >= int(rangefrom), csv_rows))
    print('filtered')
    print(filtered)
    return render_template('task11results.html', results=filtered)


@app.route('/10')
def task10():
    return render_template('hello.html')


@app.route('/12')
def form12():
    return render_template('task12.html')


@app.route('/12name', methods=['POST'])
def form12name():
    name = request.form['name']
    match = None
    for row in csv_rows:
        if row[0] == name:
            match = row
    return render_template('task12update.html', match=match)


@app.route('/12submit', methods=['POST'])
def form12submit():
    name = request.form['name']
    classname = request.form['class']
    comments = request.form['comments']
    for row in csv_rows:
        if row[0] == name:
            row[2] = classname
            row[4] = comments
    return redirect(url_for('hello_world'))


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
