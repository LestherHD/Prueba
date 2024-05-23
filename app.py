from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    app.logger.info(f"Entramos al path {request.path}")
    return render_template("index.html")


@app.route("/saludar/<nombre>/<int:edad>")
def saludar(nombre, edad):
    return render_template("saludar.html", nombre=nombre, edad=edad)


if __name__ == "__main__":
    app.run(
        "localhost",
        8009,
        debug=True,
    )
