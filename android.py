from flask import Flask, request, jsonify
import sql

app = Flask(__name__)


@app.route('/', methods=['POST'])
def order():
    result = request.json
    if 'dep' in result and 'order' in result:
        order_sql = sql.sr(sql.ord_sql % (result['order'], result['dep']))
        ordero = order_sql.fetchone()
        a = {'shipment': ordero[3]}
        orderf = order_sql.fetchall()
        for item in orderf:
            a[item[0]] = {'status': item[1], 'ready': item[2]}
        ret = a
    else:
        ret = {'status': 'error 1'}
    print(ret)  # debug
    return jsonify(ret)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
