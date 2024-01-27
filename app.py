from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/info")
def info():
    nome = request.args.get("nome","Anonimo")
    idade = request.args.get("idade","Indefinido")
    return f"nome {nome}, idade {idade}"

@app.route("/info2/<nome>/<idade>")
def info2(nome,idade):
    return f"nome {nome}, idade {idade}"
    


if __name__ == "__main__":
    app.run(debug=True)