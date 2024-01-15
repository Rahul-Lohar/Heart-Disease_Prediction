from flask import Flask, render_template, request
import pickle
app = Flask(__name__)

model = pickle.load(open('heart.pkl','rb'))

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/heart")
def price():
    v0 = float(request.args.get("Age"))
    v1 = float(request.args.get("Sex"))
    v2 = float(request.args.get("ChestPainType"))
    v3 = float(request.args.get("RestingBP"))
    v4 = float(request.args.get("Cholesterol"))
    v5 = float(request.args.get("FastingBS"))
    v6 = float(request.args.get("RestingECG"))
    v7 = float(request.args.get("MaxHR"))
    v8 = float(request.args.get("ExerciseAngina"))
    v9 = float(request.args.get("Oldpeak"))
    v10 = float(request.args.get("ST_Slope"))
    prediction = model.predict([[v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10]])
    
    if prediction[0]==0:
        return render_template('index.html', OUTPUT= '{}'.format("No"))
    else:
        return render_template('index.html', OUTPUT= '{}'.format("yes"))
if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
    
    
    
    