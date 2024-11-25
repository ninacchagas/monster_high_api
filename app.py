from flask import Flask, jsonify
import json

app = Flask(__name__)

def carrega_dados():
    with open('mh_json.json', 'r') as f:
        return json.load(f)
    
@app.route('/dados', methods=['GET'])
def obter_dados():
    dados = carrega_dados()
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)