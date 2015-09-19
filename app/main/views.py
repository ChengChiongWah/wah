from flask import render_template
from flask.ext.login import login_user, logout_user, login_required, current_user 
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
