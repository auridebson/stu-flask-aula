from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/caracteristica", methods=["POST"])
def caracteristica():
    nome = request.form.get("nome")
    idade = request.form.get("idade")
    return f"<strong>Nome:</strong> {nome} - <strong>Idade:</strong> {idade}"





@app.route("/info")
def info():
    nome = request.args.get("nome","Anonimo")
    idade = request.args.get("idade","Indefinido")
    return f"nome {nome}, idade {idade}"


@app.route("/info2")
@app.route("/info2/<string:nome>")
@app.route("/info2/<int:idade>")
@app.route("/info2/<string:nome>/<int:idade>")
def info2(nome = "Anonimo",idade = "Indefinido"):
    return f"nome {nome}, idade {idade}"
    


if __name__ == "__main__":
    app.run(debug=True)