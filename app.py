from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return """
    <html>
    <head>
    </head>
    <body>
    
    <marquee><h1>Hello World</h1></marquee>

    </body>
    </html>
    """


app.run(debug=True)