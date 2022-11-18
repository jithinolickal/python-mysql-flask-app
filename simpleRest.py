# TO RUN ----- :  python simpleRest.py
# OR
# TO RUN ----- :  export FLASK_ENV=development && python -m flask run

from flask import Flask
from db import get_all

from modules.uploadFile import fileUpload_api

app = Flask(__name__)

app.register_blueprint(fileUpload_api) # connects to uploadFile route modules

@app.route('/')
def hello_world():
   return "welcome"

@app.route('/getAll')
def get_all_data():
   data = get_all("user")
   return data

if __name__ == "__main__":
    app.run()