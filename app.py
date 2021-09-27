from flask import Flask, json, jsonify, render_template







app = Flask(__name__)



#Home
#Display count of persons and persosn properties
@app.route("/")
def home_page():
    _result={'stattus':'ok', 'message':'Well Come To API Server'}
    return jsonify(_result)

@app.route("/sendmsg/<id>")
def sendMessage(id):
    _result={'stattus':'ok', 'message':id}
    return jsonify(_result)

if __name__ == '__main__':
    app.run(debug=True, port=8090)
    

    
