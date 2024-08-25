# import necessary libraries
from flask import render_template, request 
from flask import Flask
import pickle
import numpy as np
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__,static_url_path='/assets', static_folder='templates/assets')

model = pickle.load(open('Precision_Welding_Optimization.pkl','rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/login', methods = ['POST'])

def login():
    a = request.form["pressure"]
    b = request.form["welding_time"]
    c = request.form["angle"]
    d = request.form["force"]
    e = request.form["current"]
    f = request.form["thickness_a"]
    g = request.form["thickness_b"]
    h = request.form["pull_test"]
    i = request.form["nugget_diameter"]
        
    t = [[float(a), float(b), float(c),float(d),float(e), float(f), float(g),float(h),float(i)]]
    scaled_t = scaler.transform(t)
    output = model.predict(scaled_t)
    print(output)
    
    return render_template("index.html", y = 'Expected Welding Category: '+(output[0]))
    
if __name__ == '__main__':
    app.run(debug = True)