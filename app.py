import logging
from flask import Flask
from api.api import api_blueprint
from main.views import main_blueprint

app = Flask(__name__)
app.config['JSON_AN_ASCII'] = False
app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)

logging.basicConfig(filename='logs/api.log', level=logging.INFO)

if __name__ == '__main__':
    app.run(debug=True)
