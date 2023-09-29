from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/get_deals', methods=['GET'])
def get_deals():
    # URL da API que você deseja consumir
    api_url = 'https://crm.rdstation.com/api/v1/deals?token=6400d8760a67d300105d8ace&page=1&limit=200'

    try:
        # Faz uma solicitação GET para a API
        response = requests.get(api_url)

        # Verifica se a solicitação foi bem-sucedida
        if response.status_code == 200:
            # Obtém o JSON de resposta
            data = response.json()
            return jsonify(data)

        else:
            return jsonify({'error': 'Failed to retrieve deals from the API.'}), response.status_code

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
