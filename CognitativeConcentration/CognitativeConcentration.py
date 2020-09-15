from random import randint
from flask import Flask, render_template

app = Flask(__name__)
def numbers():
    numbers = []

    size = 4#int(input("size:"))
    size **= 2

    count = 1
    d = {}

    while len(numbers) < size:
        r = randint(1, size)
        if r not in numbers:
            numbers.append(r)
            d[count] = r
            count += 1

    return [d]


@app.route('/')
def index():
    info = numbers()
    return render_template('CCindex.html', info=info)


@app.route('/results')
def res():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)