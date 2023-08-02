from flask_restful import Resource

lista_habilidades = ["PHP", "JAVASCRIPT", "JAVA", "PYTHON"]

class Habilidades(Resource):
    def get(self):
        return lista_habilidades