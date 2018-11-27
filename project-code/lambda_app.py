from flask import render_template
import connexion

app = connexion.App(__name__,specification_dir="./")
app.add_api("lambda.yaml")

@app.route("/lambda/")
def home():
    return render_template("lambda.html")


if __name__ == "__main__":
    app.run(port=8080,debug=True)