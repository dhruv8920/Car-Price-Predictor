from flask import Flask, render_template, request
import pickle
import numpy as np
from datetime import date

app = Flask(__name__)
model = pickle.load(open('car_price_regression_model.pkl', 'rb'))


@app.route('/')
def Home():
    return render_template('test.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Owner = int(request.form['Owner'])
        Fuel_Type_Petrol = request.form['Fuel_Type_Petrol']
        if(Fuel_Type_Petrol == 'Petrol'):
                Fuel_Type_Petrol = 1
                Fuel_Type_Diesel = 0

        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 1

        Year = date.today().year -Year
        Seller_Type_Individual = request.form['Seller_Type_Individual']
        if(Seller_Type_Individual == 'Individual'):
            Seller_Type_Individual = 1

        else:
            Seller_Type_Individual = 0

        Transmission_Manual = request.form['Transmission_Manual']
        if(Transmission_Manual == 'Manual'):
            Transmission_Manual = 1
        else:
            Transmission_Manual = 0
        prediction = model.predict([[Present_Price,Kms_Driven,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
        price = round(prediction[0],2)
        if price<0:
            return render_template('test.html',message="Sorry you cannot sell this car")
        else:
            return render_template('test.html',message="You Can Sell The Car at {} Lacs".format(price))

if __name__=="__main__":
    app.run(debug=True)
          
