from flask import Flask, request, jsonify
import sql

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def shipment():
    if request.method == 'POST':
        try:
            c = request.json['shipment']
        except:
            return jsonify({'status': 'wrong request'})
        else:
            sn = sql.zz("SELECT * FROM LV_Shipment WHERE shp_Code = '%s'" % c)
            item = sn.fetchone()
            if not item:
                return jsonify({'status': 'wrong shipment number'})
            else:
                print(request.json, item)
                return jsonify({'status': item[11]})
    else:
        return jsonify({'status': 'wrong method'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
