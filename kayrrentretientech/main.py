from flask import Flask, jsonify

app = Flask(__name__)

# Route for the root URL that displays a welcome message
@app.route('/')
def welcome():
    return "Bonjour, c'est le travail de Mansour Chaouki. Veuillez utiliser le chemin '/power/europe' pour accéder aux informations nécessaires."

# Route that returns the latest CO2 emission value for the power industry in Europe
@app.route('/power/europe')
def get_latest_co2_emission():
    data = {
        "country": "Europe",
        "industry": "Power",
        "unit": "MT",
        "value": 1.74
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
