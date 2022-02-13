from flask import Flask, request
import requests, json
app = Flask(__name__)

@app.route('/')
def main():
    ENDPOINT = 'https://openexchangerates.org/api/latest.json?app_id={}'.format(os.environ['OPENEXCHANGERATES'])
    data = requests.get(ENDPOINT).content
    json_data = json.loads(data)

    EUR = json_data['rates']['EUR']
    EUR_BASE = 0.9118

    GBP = json_data['rates']['GBP']
    GBP_BASE = 0.8177

    CNY = json_data['rates']['CNY']

    return 'EUR {} (0.9118) | ${} <br> GBP {} (0.8177) | ${} <br> CNY {}'.format( EUR, round(((EUR_BASE - EUR) * 5000), 2) , GBP, round(((GBP_BASE - GBP) * 5000), 2), CNY )

if __name__ == "__main__":
    app.run()