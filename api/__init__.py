# -*- coding: utf-8 -*-

from flask import Flask, jsonify

from api.database import init_app as init_db
from api.v0_1 import init_app as register_api_v0_1
import settings


versions = ['v0.1']

app = Flask(__name__)
app.config.from_object('settings')

@app.route('/')
def main():
    return jsonify(status=200,\
            code='http://github.com/teampopong/popong-api',
            issues='http://github.com/teampopong/popong-api/issues',
            documents='%s/#api' % settings.API_DOCS_URL)

@app.route('/<version>/')
def api_docs(version):
    if version in versions:
        return jsonify(status=200,
            documents='%s/api/%s' % (settings.API_DOCS_URL, version))
    else:
        return jsonify(status=404, message="Please check the API version."), 404

@app.errorhandler(401)
def error_401(error):
    return jsonify(status=401, message="Did you add an api_key?"), 401

@app.errorhandler(404)
def error_404(error):
    return jsonify(status=404, exception="That request is not valid."), 404

init_db(app)
register_api_v0_1(app)
