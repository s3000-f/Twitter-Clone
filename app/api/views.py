"""
Backend Template

Use this to display server debugging info during development

"""
from flask import render_template
from app.api import api_bp
import json
from app.api import db_handler
@api_bp.route('/')
def api():
    return render_template('api.html', msg='API Blueprint View')


@api_bp.route('/dat')
def dat():
    # inp = data_handler.getUserid("soosk")
    return db_handler.login("soosk", "piaz")

