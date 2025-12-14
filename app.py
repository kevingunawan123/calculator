from flask import Flask, render_template, request

from src import calculator

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        try:
            a = float(request.form.get("a", "0"))
            b = float(request.form.get("b", "0"))
            op = request.form.get("op", "add")

            if op == "add":
                result = calculator.add(a, b)
            elif op == "subtract":
                result = calculator.subtract(a, b)
            elif op == "multiply":
                result = calculator.multiply(a, b)
            elif op == "divide":
                result = calculator.divide(a, b)
            else:
                error = "Unknown operation."
        except ValueError as exc:
            error = str(exc)

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    # For local dev only; in production use a WSGI server.
    app.run(debug=True, port=5000)
