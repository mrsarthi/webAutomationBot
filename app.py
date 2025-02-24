from flask import Flask, render_template, request

app = Flask(__name__)

# Store submitted data
submitted_data = {}


@app.route("/", methods=["GET", "POST"])
def form():
    global submitted_data

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Store data for display
        submitted_data = {"name": name, "email": email, "message": message}

    return render_template("form.html", data=submitted_data)


if __name__ == "__main__":
    app.run(debug=True)
