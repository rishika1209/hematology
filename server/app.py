from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)

# Configure MongoDB URI (replace 'your_database_name' with your actual database name)
app.config['MONGO_URI'] = 'mongodb+srv://rishikasirnam:Atlas09@mernapp.y04pynw.mongodb.net/anemia_data?retryWrites=true&w=majority'
mongo = PyMongo(app)

model1 = joblib.load('decision_tree_modle1.joblib')
model2 = joblib.load('decision_tree_modle2.joblib')
model3 = joblib.load('random_forest_modle1.joblib')
model4 = joblib.load('random_forest_modle2.joblib')
model5 = joblib.load('logistic_modle1.joblib')
model6 = joblib.load('logistic_modle2.joblib')
model7 = joblib.load('knn_modle1.joblib')
model8 = joblib.load('knn_modle2.joblib')  
model9 = joblib.load('Svm_modle1.joblib')
model10 = joblib.load('Svm_modle2.joblib')
model11 = joblib.load('NB_modle1.joblib')
model12 = joblib.load('NB_modle2.joblib')
models = [
    
    joblib.load('decision_tree_modle2.joblib'),
   
    joblib.load('random_forest_modle2.joblib'),
    
    joblib.load('logistic_modle2.joblib'),
    
    joblib.load('knn_modle2.joblib'),
    
    joblib.load('Svm_modle2.joblib'),
    
    joblib.load('NB_modle2.joblib')
]
# API Route for predicting anemia and storing data in MongoDB
@app.route("/api", methods=["POST"])
def predict_anemia1():
    if request.method == "POST":
        data = request.get_json(force=True)
        gender = data["gender"]
        hemoglobin = float(data["hemoglobin"])
        mcv = float(data["mcv"])
        input_data1 = pd.DataFrame({"Gender": [gender], "Hemoglobin": [hemoglobin], "MCV": [mcv]})
        result = model1.predict(input_data1)

        try:
            # Store data in MongoDB
            db = mongo.db.anemia_data
            db.insert_one({
                "gender": gender,
                "hemoglobin": hemoglobin,
                "mcv": mcv,
                "result": "Anemia" if (result[0] == 1) else "No Anemia"
            })
            return jsonify({"result": "Anemia" if (result[0] == 1) else "No Anemia"})
        except Exception as e:
            return jsonify({"error": str(e)})
@app.route("/api1", methods=["POST"])
def predict_anemia2():
    if request.method == "POST":
        data = request.get_json(force=True)
        gender = data["gender"]
        hemoglobin = float(data["hemoglobin"])
        mcv = float(data["mcv"])
        mchc=float(data["mchc"])
        mch=float(data["mch"])
        input_data2 = pd.DataFrame({
                    'Gender': [gender],
                    'Hemoglobin': [hemoglobin],
                    'MCH': [mch],
                    'MCHC': [mchc],
                    'MCV': [mcv]
                    })
        result = model2.predict(input_data2)

        try:
            # Store data in MongoDB
            db = mongo.db.anemia_data
            db.insert_one({
                "gender": gender,
                "hemoglobin": hemoglobin,
                "mcv": mcv,
                "mchc":mchc,
                "mch":mch,
                "result": "Anemia" if (result[0] == 1) else "No Anemia"
            })
            return jsonify({"result": "Anemia" if (result[0] == 1) else "No Anemia"})
        except Exception as e:
            return jsonify({"error": str(e)})
@app.route("/api3", methods=["POST"])
def predict_anemia3():
    if request.method == "POST":
        data = request.get_json(force=True)
        gender = data["gender"]
        hemoglobin = float(data["hemoglobin"])
        mcv = float(data["mcv"])
        input_data3 = pd.DataFrame({"Gender": [gender], "Hemoglobin": [hemoglobin], "MCV": [mcv]})
        result = model3.predict(input_data3)

        try:
            # Store data in MongoDB
            db = mongo.db.anemia_data
            db.insert_one({
                "gender": gender,
                "hemoglobin": hemoglobin,
                "mcv": mcv,
                "result": "Anemia" if (result[0] == 1) else "No Anemia"
            })
            return jsonify({"result": "Anemic" if (result[0] == 1) else "Non Anemic"})
        except Exception as e:
            return jsonify({"error": str(e)})
@app.route("/api4", methods=["POST"])
def predict_anemia4():
    if request.method == "POST":
        data = request.get_json(force=True)
        gender = data["gender"]
        hemoglobin = float(data["hemoglobin"])
        mcv = float(data["mcv"])
        mchc=float(data["mchc"])
        mch=float(data["mch"])
        input_data4 = pd.DataFrame({
                    'Gender': [gender],
                    'Hemoglobin': [hemoglobin],
                    'MCH': [mch],
                    'MCHC': [mchc],
                    'MCV': [mcv]
                    })
        result = model4.predict(input_data4)

        try:
            # Store data in MongoDB
            db = mongo.db.anemia_data
            db.insert_one({
                "gender": gender,
                "hemoglobin": hemoglobin,
                "mcv": mcv,
                "mchc":mchc,
                "mch":mch,
                "result": "Anemia" if (result[0] == 1) else "No Anemia"
            })
            return jsonify({"result": "Anemia" if (result[0] == 1) else "No Anemia"})
        except Exception as e:
            return jsonify({"error": str(e)})
@app.route("/api5", methods=["POST"])
def predict_anemia5():
    if request.method == "POST":
        data = request.get_json(force=True)
        gender = data["gender"]
        hemoglobin = float(data["hemoglobin"])
        mcv = float(data["mcv"])
        input_data5 = pd.DataFrame({"Gender": [gender], "Hemoglobin": [hemoglobin], "MCV": [mcv]})
        result = model5.predict(input_data5)

        try:
            # Store data in MongoDB
            db = mongo.db.anemia_data
            db.insert_one({
                "gender": gender,
                "hemoglobin": hemoglobin,
                "mcv": mcv,
                "result": "Anemia" if (result[0] == 1) else "No Anemia"
            })
            return jsonify({"result": "Anemia" if (result[0] == 1) else "No Anemia"})
        except Exception as e:
            return jsonify({"error": str(e)})
@app.route("/api6", methods=["POST"])
def predict_anemia6():
    if request.method == "POST":
        data = request.get_json(force=True)
        gender = data["gender"]
        hemoglobin = float(data["hemoglobin"])
        mcv = float(data["mcv"])
        mchc=float(data["mchc"])
        mch=float(data["mch"])
        input_data6 = pd.DataFrame({
                    'Gender': [gender],
                    'Hemoglobin': [hemoglobin],
                    'MCH': [mch],
                    'MCHC': [mchc],
                    'MCV': [mcv]
                    })
        result = model6.predict(input_data6)

        try:
            # Store data in MongoDB
            db = mongo.db.anemia_data
            db.insert_one({
                "gender": gender,
                "hemoglobin": hemoglobin,
                "mcv": mcv,
                "mchc":mchc,
                "mch":mch,
                "result": "Anemia" if (result[0] == 1) else "No Anemia"
            })
            return jsonify({"result": "Anemia" if (result[0] == 1) else "No Anemia"})
        except Exception as e:
            return jsonify({"error": str(e)})
@app.route("/api7", methods=["POST"])
def predict_anemia7():
    if request.method == "POST":
        data = request.get_json(force=True)
        gender = data["gender"]
        hemoglobin = float(data["hemoglobin"])
        mcv = float(data["mcv"])
        input_data7 = pd.DataFrame({"Gender": [gender], "Hemoglobin": [hemoglobin], "MCV": [mcv]})
        result = model7.predict(input_data7)

        try:
            # Store data in MongoDB
            db = mongo.db.anemia_data
            db.insert_one({
                "gender": gender,
                "hemoglobin": hemoglobin,
                "mcv": mcv,
                "result": "Anemia" if (result[0] == 1) else "No Anemia"
            })
            return jsonify({"result": "Anemia" if (result[0] == 1) else "No Anemia"})
        except Exception as e:
            return jsonify({"error": str(e)})
@app.route("/api8", methods=["POST"])
def predict_anemia8():
    if request.method == "POST":
        data = request.get_json(force=True)
        gender = data["gender"]
        hemoglobin = float(data["hemoglobin"])
        mcv = float(data["mcv"])
        mchc=float(data["mchc"])
        mch=float(data["mch"])
        input_data8 = pd.DataFrame({
                    'Gender': [gender],
                    'Hemoglobin': [hemoglobin],
                    'MCH': [mch],
                    'MCHC': [mchc],
                    'MCV': [mcv]
                    })
        result = model8.predict(input_data8)

        try:
            # Store data in MongoDB
            db = mongo.db.anemia_data
            db.insert_one({
                "gender": gender,
                "hemoglobin": hemoglobin,
                "mcv": mcv,
                "mchc":mchc,
                "mch":mch,
                "result": "Anemia" if (result[0] == 1) else "No Anemia"
            })
            return jsonify({"result": "Anemia" if (result[0] == 1) else "No Anemia"})
        except Exception as e:
            return jsonify({"error": str(e)})
@app.route("/api9", methods=["POST"])       
def predict_anemia9():
    if request.method == "POST":
        data = request.get_json(force=True)
        gender = data["gender"]
        hemoglobin = float(data["hemoglobin"])
        mcv = float(data["mcv"])
        input_data9 = pd.DataFrame({"Gender": [gender], "Hemoglobin": [hemoglobin], "MCV": [mcv]})
        result = model9.predict(input_data9)

        try:
            # Store data in MongoDB
            db = mongo.db.anemia_data
            db.insert_one({
                "gender": gender,
                "hemoglobin": hemoglobin,
                "mcv": mcv,
                "result": "Anemic" if (result[0] == 1) else "Non Anemic"
            })
            return jsonify({"result": "Anemia" if (result[0] == 1) else "No Anemia"})
        except Exception as e:
            return jsonify({"error": str(e)})
@app.route("/api10", methods=["POST"])
def predict_anemia10():
    if request.method == "POST":
        data = request.get_json(force=True)
        gender = data["gender"]
        hemoglobin = float(data["hemoglobin"])
        mcv = float(data["mcv"])
        mchc=float(data["mchc"])
        mch=float(data["mch"])
        input_data10 = pd.DataFrame({
                    'Gender': [gender],
                    'Hemoglobin': [hemoglobin],
                    'MCH': [mch],
                    'MCHC': [mchc],
                    'MCV': [mcv]
                    })
        result = model10.predict(input_data10)

        try:
            # Store data in MongoDB
            db = mongo.db.anemia_data
            db.insert_one({
                "gender": gender,
                "hemoglobin": hemoglobin,
                "mcv": mcv,
                "mchc":mchc,
                "mch":mch,
                "result": "Anemia" if (result[0] == 1) else "No Anemia"
            })
            return jsonify({"result": "Anemia" if (result[0] == 1) else "No Anemia"})
        except Exception as e:
            return jsonify({"error": str(e)})
@app.route("/api11", methods=["POST"])
def predict_anemia11():
    if request.method == "POST":
        data = request.get_json(force=True)
        gender = data["gender"]
        hemoglobin = float(data["hemoglobin"])
        mcv = float(data["mcv"])
        input_data11 = pd.DataFrame({"Gender": [gender], "Hemoglobin": [hemoglobin], "MCV": [mcv]})
        result = model11.predict(input_data11)

        try:
            # Store data in MongoDB
            db = mongo.db.anemia_data
            db.insert_one({
                "gender": gender,
                "hemoglobin": hemoglobin,
                "mcv": mcv,
                "result": "Anemia" if (result[0] == 1) else "No Anemia"
            })
            return jsonify({"result": "Anemia" if (result[0] == 1) else "No Anemia"})
        except Exception as e:
            return jsonify({"error": str(e)})
@app.route("/api12", methods=["POST"])
def predict_anemia12():
    if request.method == "POST":
        data = request.get_json(force=True)
        gender = data["gender"]
        hemoglobin = float(data["hemoglobin"])
        mcv = float(data["mcv"])
        mchc=float(data["mchc"])
        mch=float(data["mch"])
        input_data12 = pd.DataFrame({
                    'Gender': [gender],
                    'Hemoglobin': [hemoglobin],
                    'MCH': [mch],
                    'MCHC': [mchc],
                    'MCV': [mcv]
                    })
        result = model12.predict(input_data12)

        try:
            # Store data in MongoDB
            db = mongo.db.anemia_data
            db.insert_one({
                "gender": gender,
                "hemoglobin": hemoglobin,
                "mcv": mcv,
                "mchc":mchc,
                "mch":mch,
                "result": "Anemia" if (result[0] == 1) else "No Anemia"
            })
            return jsonify({"result": "Anemia" if (result[0] == 1) else "No Anemia"})
        except Exception as e:
            return jsonify({"error": str(e)})     
@app.route("/api13", methods=["POST"])
def predict_anemia13():
    if request.method == "POST":
        data = request.get_json(force=True)
        gender = data["gender"]
        hemoglobin = float(data["hemoglobin"])
        mcv = float(data["mcv"])
        mchc = float(data["mchc"])
        mch = float(data["mch"])

        responses = []

        for model in models:
            input_data = pd.DataFrame({
                'Gender': [gender],
                'Hemoglobin': [hemoglobin],
                'MCH': [mch],
                'MCHC': [mchc],
                'MCV': [mcv]
            })

            result = model.predict(input_data)

            try:
                # Store data in MongoDB
                db = mongo.db.anemia_data
                db.insert_one({
                    "gender": gender,
                    "hemoglobin": hemoglobin,
                    "mcv": mcv,
                    "mchc": mchc,
                    "mch": mch,
                    "result": "Anemia" if (result[0] == 1) else "No Anemia",
                    "model_name": "Model Name"  # You may want to add a model name or identifier
                })

                responses.append({
                    "result": "Anemia" if (result[0] == 1) else "No Anemia",
                    "model_name": "Model Name"  # You may want to add a model name or identifier
                })

            except Exception as e:
                responses.append({"error": str(e)})

        return jsonify(responses)

if __name__ == "__main__":
    app.run(debug=True)