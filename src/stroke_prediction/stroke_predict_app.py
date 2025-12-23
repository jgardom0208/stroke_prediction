import pickle
from flask import Flask, jsonify, request
from stroke_predict_service import predict_single

app = Flask('stroke-prediction')

# Cargamos el modelo SVM y el vectorizador que guardamos en el paso anterior
with open('models/stroke-model.pck', 'rb') as f:
    dv, model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    # Recibimos el JSON con los datos del paciente
    patient = request.get_json()
    
    # Llamamos a la función de predicción
    stroke, prediction = predict_single(patient, dv, model)

    # Preparamos la respuesta
    result = {
        'stroke': stroke,
        'stroke_probability': round(prediction, 3),
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=8000)