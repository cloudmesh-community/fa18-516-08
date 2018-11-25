from flask import Flask,render_template,request
import connexion
app = connexion.App(__name__,specification_dir="./")
app.add_api("lambda.yaml")
@app.route("/")
def home():
    return render_template("welcome.html")
if __name__ == "__main__":
    app.run(port=5555,debug=True)