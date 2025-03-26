from flask import Flask,jsonify,request

app = Flask(__name__)

livros = [
   
    {"id": 1, "titulo": "1984", "autor": "George Orwell"},
    {"id": 2, "titulo": "Dom Quixote", "autor": "Miguel de Cervantes"},
    {"id": 3, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien"},
    {"id": 4, "titulo": "Orgulho e Preconceito", "autor": "Jane Austen"},
    {"id": 5, "titulo": "Crime e Castigo", "autor": "Fiódor Dostoiévski"},
    {"id": 6, "titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry"},
    {"id": 7, "titulo": "Harry Potter e a Pedra Filosofal", "autor": "J.K. Rowling"},
    {"id": 8, "titulo": "O Alquimista", "autor": "Paulo Coelho"},
    {"id": 9, "titulo": "A Revolução dos Bichos", "autor": "George Orwell"},
    {"id": 10, "titulo": "Moby Dick", "autor": "Herman Melville"}
]

@app.route('/livros',methods = ['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>',methods = ['GET'])
def obter_unico_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
@app.route('/livros/<int:id>',methods = ['PUT'])
def alterar_livro(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

@app.route('/livros',methods=["POST"])    
def incluir_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

@app.route('/livros/<int:id>',methods = ['DELETE'])
def excluir_livro(id):
    for indice,livro in enumerate(livros):
        if livro.get('id')==id:
            del livros[indice]

    return jsonify(livros)
app.run(port=2000,host='localhost',debug=True)