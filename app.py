from flask import flask
app = Flask(__name__)

@app.route('/')
def hello()
  return "Halo dari Flask+Docker+Jenkins!"

if__name__=='__main__':
    app.run(host='0.0.0.0', port=5000)