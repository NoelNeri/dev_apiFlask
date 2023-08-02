import json

from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades


app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id':10,
    'nome':'Noel',
    'habilidades':['IPM', 'Devteam', 'analista']},
    {'id':20,
    'nome':'Neri',
    'habilidades':['DBA', 'Programador', 'arquiteto']
     }]

# Recebe ID e consulta, altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        print(id)
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} nao existe.'.format(id)
            response = {'status': 'Erro01', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador dessa frent'.format(id)
            response = {'status': 'Erro02', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'Sucesso','mensagem':'Registro Excluido'}


# Lista todos os desenvolvedores e inclui um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)
