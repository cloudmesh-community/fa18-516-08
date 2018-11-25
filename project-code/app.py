import os
from flask import Flask,render_template,request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
@app.route("/")
def welcome():
    return render_template("upload.html")

@app.route("/upload", methods =["POST"])
def upload():
    target_path = os.path.join(ROOT_PATH,'LambdaDeployment/')
    print(target_path)
    if not os.path.isdir(target_path):
        os.mkdir(target_path)

    for f in request.files.getlist("file"):
        #f = request.files("file")
        print(f)
        filename = f.filename
        print(filename)
        dest = "/".join([target_path,filename])
        f.save(dest)

    return render_template("success.html")

if __name__ == "__main__":
    app.run(port=5000,debug=True)

