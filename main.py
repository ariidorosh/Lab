from flask import Flask, jsonify

app = Flask(__name__)

app.config['DEBUG'] = False


@app.route('/api/v1/hello-world-9', methods=['GET'])
def hello_world_9():
    response = {
        'message': 'Hello World 9'
    }
    return jsonify(response), 200


app.run(debug=True)
