from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Save data (can be stored in a database)
        with open("responses.txt", "a") as f:
            f.write(f"Name: {name}, Email: {email}, Message: {message}\n")

        return "Form submitted successfully!"

    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)
