from random import randint
from flask import Flask, render_template

app = Flask(__name__)
def numbers():
    numbers = []

    size = 4#int(input("size:"))
    size **= 2

    count = 1
    d = {}
    t = []

    while len(numbers) < size:
        r = randint(1, size)
        if r not in numbers:
            numbers.append(r)
            d[count] = r
            count += 1
    print(numbers)
    print(d)
    print(t.append(d))

    return [d]
'''
[
    {'stat_name': 'Dublin Heuston', 'origin': 'Dublin Heuston', 'destination': 'Athlone', 'departure': '17:10', 'arrival': '18:45', 'due': '80', 'late': '0'}, 
    {'stat_name': 'Dublin Heuston', 'origin': 'Dublin Heuston', 'destination': 'Cork', 'departure': '16:00', 'arrival': '18:37', 'due': '10', 'late': '0'}, 
    {'stat_name': 'Dublin Heuston', 'origin': 'Dublin Heuston', 'destination': 'Cork', 'departure': '17:00', 'arrival': '19:32', 'due': '70', 'late': '0'}, 
    {'stat_name': 'Dublin Heuston', 'origin': 'Cork', 'destination': 'Dublin Heuston', 'departure': '13:25', 'arrival': '15:59', 'due': '17', 'late': '8'}, 
    {'stat_name': 'Dublin Heuston', 'origin': 'Portlaoise', 'destination': 'Dublin Heuston', 'departure': '15:25', 'arrival': '16:33', 'due': '47', 'late': '4'}, 
    {'stat_name': 'Dublin Heuston', 'origin': 'Westport', 'destination': 'Dublin Heuston', 'departure': '13:10', 'arrival': '16:27', 'due': '48', 'late': '11'}, 
    {'stat_name': 'Dublin Heuston', 'origin': 'Cork', 'destination': 'Dublin Heuston', 'departure': '14:25', 'arrival': '16:59', 'due': '71', 'late': '2'}, 
    {'stat_name': 'Dublin Heuston', 'origin': 'Waterford', 'destination': 'Dublin Heuston', 'departure': '14:50', 'arrival': '17:07', 'due': '77', 'late': '0'},
    {'stat_name': 'Dublin Heuston', 'origin': 'Dublin Heuston', 'destination': 'Galway', 'departure': '16:30', 'arrival': '18:50', 'due': '40', 'late': '0'}, 
    {'stat_name': 'Dublin Heuston', 'origin': 'Dublin Heuston', 'destination': 'Limerick', 'departure': '16:25', 'arrival': '18:40', 'due': '35', 'late': '0'}, 
    {'stat_name': 'Dublin Heuston', 'origin': 'Dublin Heuston', 'destination': 'Portlaoise', 'departure': '16:20', 'arrival': '17:30', 'due': '30', 'late': '0'}
]

'''


@app.route('/')
def index():
    info = numbers()
    print(f"-->{info}")
    return render_template('CCindex.html', info=info)


if __name__ == '__main__':
    # numbers()
    app.run(port=5000, debug=True)