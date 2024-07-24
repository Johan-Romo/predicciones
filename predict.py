import sys
import json
import pickle
import numpy as np

# Cargar el modelo y el escalador
modelo = pickle.load(open('modelo_svm_rbf.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

def predict(data):
    valores = np.array([[
        int(data['edad']), int(data['tipo_empleado']), int(data['fnlwgt']),
        int(data['educacion']), int(data['educacion_num']), int(data['estado_civil']),
        int(data['ocupacion']), int(data['relacion']), int(data['raza']),
        int(data['sexo']), int(data['capital_ganado']), int(data['capital_perdido']),
        int(data['hr_por_semana']), int(data['pais'])
    ]])
    valores_scaled = scaler.transform(valores)
    prediccion = modelo.predict(valores_scaled)
    return prediccion[0]

if __name__ == '__main__':
    data = json.loads(sys.argv[1])
    result = predict(data)
    print(result)