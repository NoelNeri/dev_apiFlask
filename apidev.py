import json

from flask import Flask, jsonify, request

app = Flask(__name__)

desenvolvedores = [
    {'id':10,
    'nome':'Noel',
    'habilidades':['IPM', 'Devteam', 'analista']},
    {'id':20,
    'nome':'Neri',
    'habilidades':['DBA', 'Programador', 'arquiteto']
     }]


# Recebe ID e consulta, altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} nao existe.'.format(id)
            response = {'status':'Erro01', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador dessa frent'.format(id)
            response = {'status':'Erro02','mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'Sucesso','mensagem':'Registro Excluido'})

# Lista todos os desenvolvedores e inclui um novo desenvolvedor
@app.route('/dev/', methods=['POST','GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        mensagem = 'Registro inserido.'.format(id)
        response = {'status': 'Sucesso', 'mensagem': mensagem}
        return jsonify(response, desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)
