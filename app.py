from flask import Flask, jsonify, request
import json
app = Flask(__name__)

@app.route('/<int:id>')
def pessoa(id):
    soma = 1 + id
    return jsonify({'id': id, 'nome':'Arthur'})

# @app.route('/soma/<int:v1>/<int:v2>/')
# def soma(v1,v2):
#     return {'soma': v1 + v2}


@app.route('/soma', methods= ['POST', 'PUT', 'GET'] )
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10+10

    return {'soma': total}

if __name__ == '__main__':
    app.run(debug=True)