from flask import Flask, jsonify, request, Response
from tax_calculator import Calculator
app = Flask(__name__)


def valid_data(object):
    return True if "value" in object else False


money_amount = [];

@app.route("/value", methods=["POST"])
def input_calc_value():
    data = request.get_json()
    if valid_data(data):
        new_data = {
            "value": data["value"]
        }
        c = Calculator(new_data)
        money_amount.insert(0, c.calculate_tax)
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = "/value/" + str(new_data["value"])
        return response
    else:
        invalidDataObjectErrorMsg = {
            "error": " Invalid object passed in request ",
            "helpString": " Data passed is similiar to this {'value' : 'number' } "
        }
        response = Response(invalidDataObjectErrorMsg, status = 400, mimetype='application/json')
        return response


@app.route("/value")
def output_calc_value():
    if len(money_amount) == 0:
        send_data ={}
    else:
        send_data = {
            "value": money_amount[0]
        }
        response = jsonify(send_data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


app.run(port=5000)