from flask import Flask, request, render_template, url_for
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge, Lasso, RidgeCV, LassoCV, ElasticNetCV,ElasticNet,LinearRegression
from sklearn.model_selection import train_test_split
import pickle
app = Flask(__name__)

@app.route('/' ,methods=['GET', 'POST'])
def home():
    answer = None
    if request.method == 'POST':
        Model = request.form['model']
        Processtemperature = float(request.form['Processtemperature'])
        Rotationalspeed = float(request.form['Rotationalspeed'])
        Torque = float(request.form['Torque'])
        Toolwear = float(request.form['Toolwear'])
        Machinefailure = float(request.form['Machinefailure'])
        TWF = float(request.form['TWF'])
        HDF = float(request.form['HDF'])
        PWF = float(request.form['PWF'])
        HDF = float(request.form['OSF'])
        PWF = float(request.form['RNF'])
        p = [[Processtemperature, Rotationalspeed, Toolwear, TWF, HDF, PWF]]

        if Model == 'linear':
            lr = pickle.load(open('linearreggressionpkl', 'rb'))
            answer = lr.predict(p)[0]
        if Model == 'lasso':
            lr = pickle.load(open('lassocvreg', 'rb'))
            answer = lr.predict(p)[0]
        if Model == 'ridge':
            lr = pickle.load(open('ridgecv', 'rb'))
            answer = lr.predict(p)[0]
        if Model == 'elasticnet':
            lr = pickle.load(open('elasticcv', 'rb'))
            answer = lr.predict(p)[0]




    return render_template('main.html', data = answer)


@app.route('/profile')
def profiling():
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=True)