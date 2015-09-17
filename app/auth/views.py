from flask import render_template, url_for
from . import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html') 
