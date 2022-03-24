from flask import Flask 
app = Flask(__name__)


app.config.from_object('core.config.SECRET_KEY')
app.config.from_object('core.config.ProductionConfig')


config = app.config
from core.library.cryptography import Cryptography
# from core.library.helper import Helper
# from core.model.Log import Log

current_app = app

#from core import routes
from core.controller.UserController import app as user
app.register_blueprint(user, url_prefix='')


from core.controller.CRUDController import app as crud
app.register_blueprint(crud, url_prefix='')

