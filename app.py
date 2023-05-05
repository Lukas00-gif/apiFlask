from flask import Flask, jsonify, request, make_response

from bd import Livros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# consultar todos os livros(GET)
@app.get('/livros')
def obter_livro():
    return jsonify(Livros)

#consultar por id(GET)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in Livros:
        if livro.get('id') == id:
            return make_response(jsonify(livro))

#editar (PUT)
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    #enviados do usuario para a API
    livro_alterado = request.get_json()
    #aqui deve ser iterar
    #enumerar de acordo com o indice dos livros
    #dessa forma tenho tando o indice quando o livro individual
    for i, livro in enumerate(Livros):
        #verificar se o id atual e o id q foi solicitado
        if livro.get('id') == id:
            Livros[i].update(livro_alterado)
            return make_response(jsonify(Livros[i]))

#criar (POST)
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    Livros.append(novo_livro)

    return make_response(jsonify(Livros))


#deletar(DELETE)
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    #exclui de acodo com o indice e o id
    for i, livro in enumerate(Livros):
        if livro.get('id') == id:
            del Livros[i]
    
    return make_response(jsonify(Livros))


app.run()