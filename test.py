from flask import Flask, request, jsonify
import sql

app = Flask(__name__)


@app.route('/', methods=['POST'])
def shipment():
   print(request.headers)
   print(request.content_type)
   print(request.data)

   return jsonify({'status': 11111})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
