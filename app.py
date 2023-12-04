from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('newmodel.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/predict',methods=['POST'])
def predict_thyroid():
   Age = float(request.form.get('age',False))
   Sex = float(request.form.get('sex',False))
   On_thyroxine = float(request.form.get('on thyroxine',False))
   Query_on_thyroxine = float(request.form.get('query on thyroxine',False))
   On_antithyroid_medication = float(request.form.get('on antithyroid medication',False))
   Sick = float(request.form.get('sick',False))
   pregnant = float(request.form.get('pregnant',False))
   Thyroid_surgery = float(request.form.get('thyroid surgery',False))
   I131_treatment = float(request.form.get('I131 treatment',False))
   Query_hypothyroid = float(request.form.get('query hypothyroid',False))
   Query_hyperthyroid = float(request.form.get('query hyperthyroid',False))
   Lithium = float(request.form.get('lithium',False))
   Goiter = float(request.form.get('goiter',False))
   Tumor = float(request.form.get('tumor',False))
   hypopituitary = float(request.form.get('hypopituitary',False))
   psych = float(request.form.get('psych',False))
   TSH = float(request.form.get('TSH',False))
   T3 = float(request.form.get('T3',False))
   T4U = float(request.form.get('T4U',False))
   FTI = float(request.form.get('FTI',False))

   '''values = ({"age": Age, "sex": Sex,
              "TSH": TSH, "T3": T3, "T4U": T4U, "FTI": FTI,
              "on thyroxine": On_thyroxine, "query on thyroxine": Query_on_thyroxine,
              "on antithyroid medication": On_antithyroid_medication,
              "sick": Sick, "pregnant": pregnant, "thyroid surgery": Thyroid_surgery,
              "I131_treatment": I131_treatment,
              "query hypothyroid": Query_hypothyroid, "query hyperthyroid": Query_hyperthyroid,
              "lithium": lithium, "goitre": goitre, "tumor": tumor,
              "hypopituitary": hypopituitary,
              "psych": psych})'''



   #Prediction
   arr = (np.array([[Age,Sex,On_thyroxine,Query_on_thyroxine,On_antithyroid_medication,Sick,pregnant,Thyroid_surgery,I131_treatment,Query_hypothyroid,Query_hyperthyroid,Lithium,Goiter,Tumor,hypopituitary,psych,TSH,T3,T4U,FTI]]))

   result  = model.predict(arr)[0]


   if result == 0:
      result = 'Thyroid is absent'
   else:
      result = 'Thyroid is present'
   return render_template('result.html', prediction_text='Result: {}'.format(result))
   #return  render_template('index2.html',result = result)


if __name__=='__main__':
    app.run(debug=True)

