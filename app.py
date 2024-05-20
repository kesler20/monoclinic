from flask import render_template
from flask import Flask

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<route>/", methods=["POST", "GET"])
def show(route):
    page = {
        "home": "index",
        "product_overview": "product_overview",
        "case_studies": "case_studies",
        "contact": "contact",
    }.get(route, "404")
    return render_template(f"{page}.html")


if __name__ == "__main__":
    app.run(debug=True, port=5500)
