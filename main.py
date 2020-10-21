from flask import Flask
import database
import config
app = Flask(__name__)

app.config.from_object(config)

from controller.user.user import *

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=9990, debug=True)