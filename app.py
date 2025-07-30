from flask import Flask, request, redirect, render_template
from xrun import *  # твои функции: bain(), into()
import requests
from config import *  # импортируем переменную a из config.py
api_key='f4a246e546e000ec483798a9a74f11c7'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html', data=bain())

@app.route('/xron', methods=['POST'])
def xron():
    return render_template('index.html', data=bain())

@app.route('/pgd', methods=['POST'])
def pgd():
        url = f"http://api.openweathermap.org/data/2.5/weather?q={a}&appid={api_key}&units=metric&lang=ru"

        response = requests.get(url)

        if (response.status_code == 200): 
            data=response.json()
            name=data['name']
            temp=data['main']['temp']
            oshu=data['main']['feels_like']
        else:
            return "Ошибка при получении данных о погоде."
            
        return render_template('pgd.html', name=name, oshu=int(oshu), temp=int(temp))

@app.route('/add', methods=['POST'])
def add_user():
    try:
        id = int(request.form['id'])
        name = request.form['name']
        login = request.form['login']
        password = request.form['password']
        into(id, name, login, password)
        return redirect('/')
    except Exception as e:
        return f"<h3>Ошибка при добавлении: {e}</h3>"
@app.route('/delete', methods=['POST'])
def delete_user():
    user_id = int(request.form['id'])
    delete(user_id)  # ты должен реализовать эту функцию в xrun.py
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
