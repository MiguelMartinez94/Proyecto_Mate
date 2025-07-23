from flask import Flask, render_template, request
from utils import runge_kutta, newton_raphson

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    metodo = request.form['metodo']
    funcion = request.form['funcion']

    if metodo == 'runge_kutta':
        t0 = float(request.form['t0'])
        y0 = float(request.form['y0'])
        tf = float(request.form['tf'])
        h = float(request.form['h'])
        t_vals, y_vals = runge_kutta(funcion, t0, y0, tf, h)
        return render_template('resultados.html', metodo=metodo, funcion=funcion, t=t_vals, y=y_vals)

    elif metodo == 'newton_raphson':
        derivada = request.form['derivada']
        x0 = float(request.form['x0'])
        tol = float(request.form['tol'])
        raiz = newton_raphson(funcion, derivada, x0, tol)
        return render_template('resultados.html', metodo=metodo, funcion=funcion, raiz=raiz)

    return 'Método no válido'

if __name__ == '__main__':
    app.run(debug=True, port=8888)