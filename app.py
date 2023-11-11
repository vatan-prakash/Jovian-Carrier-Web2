from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello,Flask World!</p>"

# print(__name__)
if __name__ == '__main__':
    # print("yes")
  app.run(host='0.0.0.0', debug= True)