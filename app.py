from flask import Flask, render_template,request
from datetime import date
import numpy as np
import pickle

model = pickle.load(open('car_price_regression_model.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
def home():
    render_template('index.html')


@app.route('/predict', method = ['POST'])
def predict():
    if request.method == 'POST':

        year = int(request.form['Year'])
        cur_date = date.today()
        year = cur_date.year - year
        present_price = float(request.form['Present_Price'])
        kms_driven = int(request.form['Kms_Driven'])
        owner = int(request.form['Owner'])
        fuel_type_petrol = request.form['Fuel_Type_Petrol']

        if fuel_type_petrol == 'Petrol':
            fuel_type_petrol = 1
            fuel_type_diesel = 0

        elif fuel_type_petrol == 'Diesel':
            fuel_type_diesel = 1
            fuel_type_petrol = 0

        else:
            fuel_type_diesel = 0
            fuel_type_petrol = 0

        seller_type_individual = request.form['Seller_Type_Individual']
        if seller_type_individual == 'Individual':
            seller_type_individual = 1

        else:
            seller_type_individual = 0

        transmission_manual = request.form['Transmission_Manual']
        if transmission_manual == 'Manual':
            transmission_manual = 1

        else:
            transmission_manual = 0

        data = np.array([['present_price','kms_driven','owner','year','fuel_type_diesel','fuel_type_petrol','seller_type_individual','transmission_manual']])
        prediction = model.predict(data)
        price = round(prediction[0],2)

        if price > 0 :
            render_template('index.html',text = "You Cannot Sell this Car.")

        else:
            render_template('index.html',text ="The Estimated Price is {}".format(price))


if __name__ == "__main__":
    app.run(debug = True)