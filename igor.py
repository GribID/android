from flask import Flask, request, jsonify
import sql

app = Flask(__name__)


@app.route('/', methods=['POST'])
def shipment():
    ship_number = request.json['shipment']
    if not ship_number:
        return jsonify({'status': 'wrong request'})
    else:
        ship_status_sql = sql.sr("SELECT * FROM LV_Shipment WHERE shp_Code = '%s'" % ship_number)
        ship_status = ship_status_sql.fetchone()
        if not ship_status:
            return jsonify({'status': 'wrong shipment number'})
        else:
            print(request.json, ship_status)  # for testing
            return jsonify({'status': ship_status[11]})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
