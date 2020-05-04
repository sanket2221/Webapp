import numpy as np
from flask import Flask,request,render_template
import pickle
app = Flask(__name__)
model = pickle.load(open('regressor.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    data = int(request.form['exp'])

    prediction = model.predict(np.array([data]).reshape(1,-1))

    return render_template('index.html',prediction_text ='Salary should be Rs.{}'.format(prediction))

if __name__=='__main__':
    app.run(debug=True)