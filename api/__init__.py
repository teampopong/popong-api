# -*- coding: utf-8 -*-

from flask import Flask

from api.database import init_app as init_db
from api.v0_1 import init_app as register_api_v0_1


app = Flask(__name__)
app.config.from_object('settings')

init_db(app)
register_api_v0_1(app)

