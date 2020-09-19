from random import randint
from flask import Flask, render_template, request

app = Flask(__name__)
def numbers(num_nums=4):
    numbers = []

    size = num_nums
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


# @app.route('/')
# def index():
#     info = numbers()
#     return render_template('CCindex.html', info=info[0])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        print(text, type(text))
        table_nums = int(text)

        info = numbers(table_nums)
    else:
        info = numbers()
        table_nums = 4

    return render_template('CCindex.html', info=info[0], num_rows=table_nums)



@app.route('/results')
def res():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)