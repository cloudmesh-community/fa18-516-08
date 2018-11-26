from flask import Flask,render_template,request
import connexion
import os
import config
app = connexion.App(__name__,specification_dir="./")
app.add_api("lambda.yaml")
@app.route("/lambda/")
def home():
    return render_template("lambda.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5555,debug=True)