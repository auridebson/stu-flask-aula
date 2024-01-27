

def index():
    return render_template("index.html")

def info():
    nome = request.args.get("nome")
    idade = request.args.get("idade")
    
    return f"nome {nome}, idade{idade}"