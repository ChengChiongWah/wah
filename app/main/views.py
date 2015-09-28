from datetime import datetime
from flask import render_template, flash, redirect, url_for
from flask.ext.login import login_user, logout_user, login_required, current_user 
from . import main
from .. import db
from .forms import EditProfileForm
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)

@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
	current_user.location = form.location.data
	current_user.about_me = form.about_me.data
	db.session.add(current_user)
	db.session.commit()
	flash('Your profile has been updated.')
	return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)

@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
	user.username = form.username.data
	user.confirmed = form.confirmed.data
	user.role = Role.query.get(form.role.data)
	user.name = form.name.data
	user.location = form.location.data
	user.about_me = form.about_me.data
	db.session.add(user)
	flash('The profile has been updated.')
	return redirect(url_for('.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    db.session.commit()
    return rneder_template('edit_profile.html', form=form, user=user)

