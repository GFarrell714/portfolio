from flask import Flask,request, url_for, redirect, render_template  ## importing necessary libraries
import pandas as pd  ## to convert the input data into a dataframe for giving as a input to the model
import joblib
# from sklearn.externals import joblib

app = Flask(__name__)  ## setting up flask name

model = joblib.load("grid.joblib") ##loading model


# @app.route('/')             ## Defining main index route
# def home():
#     return render_template("index.html")   ## showing index.html as homepage


@app.route('/',methods=['POST','GET'])  ## this route will be called when predict button is called
def predict():
    if request.method =='POST':

        Age = request.form.get('Age')    
        Gender = request.form.get('Gender')
        Polyuria = request.form.get('Polyuria')
        Polydipsia = request.form.get('Polydipsia')
        sudden_weight_loss = request.form.get('Sudden Weight Loss')
        weakness = request.form.get('Weakness')
        Polyphagia = request.form.get('Polyphagia')
        Genital_thrush = request.form.get('Genital Thrush')
        visual_blurring = request.form.get('Visual Blurring')
        Itching = request.form.get('Itching')
        Irritability = request.form.get('Irritability')
        delayed_healing = request.form.get('Delayed Healing')
        partial_paresis = request.form.get('Partial Paresis')
        muscle_stiffness = request.form.get('Muscle Stiffness')
        Alopecia = request.form.get('Alopecia')
        Obesity = request.form.get('Obesity')

    
        new_row_df = pd.DataFrame([pd.Series([Age, Gender, Polyuria, Polydipsia, sudden_weight_loss, weakness, Polyphagia, Genital_thrush, visual_blurring, Itching, Irritability, delayed_healing, partial_paresis, muscle_stiffness, Alopecia, Obesity])])  ### Creating a dataframe using all the values
        print(new_row_df)
        prediction=model.predict_proba(new_row_df) ## Predicting the output
        output='{0:.{1}f}'.format(prediction[0][1], 2)    ## Out Formatting

        if output>str(0.5):
            return render_template('index.html',pred='Risk for developing diabetes: HIGH!!!')
        else:
            return render_template('index.html',pred='Risk for developing diabetes: LOW')
    else:
        return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)          ## Running the app as debug==True
