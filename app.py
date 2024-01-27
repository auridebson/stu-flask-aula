from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome")
        peso = request.form.get("peso")
        altura = request.form.get("altura")

        # < 16,9 - Muito abaixo do peso
        # 17 a 18,4 - abaixo do peso

        # 18,5 a 24,9 - peso normal
        # 25 a 29,9 - acima do peso

        # 30 a 34,9 - obesidade grau 1
        # 35 a 40 - obesidade grau 2
        # > 40 - obesidade grau 3

        # IMC = peso/(altura x altura)

        if float(peso/altura*altura) > 20:
            return f"""
            <script>
                alert("{nome}, você está bonitão... se mantenha assim.");
                window.location.href = "/"
            </script>
            """
        elif float(peso/altura*altura) < 20:
            return f"""
            <script>
                alert("{nome}, você está raquítico - coma mais.");
                window.location.href = "/"
            </script>
            """

    return render_template("index.html")

@app.route("/", methods=["POST"])
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