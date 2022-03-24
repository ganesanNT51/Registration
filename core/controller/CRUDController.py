from flask import Flask, request, Blueprint, jsonify, redirect, url_for,flash, render_template,session
from core.model.UserModel import UserModel

from core.model.CRUDModel import CRUDModel
from random import randint
import datetime

from datetime import timedelta,date,datetime
# from .. import Cryptography
from flask import session, app

import ast



app = Blueprint('crud', __name__)


@app.route('/insert_user')
def InsertUser():
	return render_template('crud/insert_user.html')

@app.route('/post_insert_user', methods = ["POST"])
def PostInsertUser():
	name      = request.form['name']
	email     = request.form['email']
	mobile    = request.form['mobile']
	password  = request.form['password']
	data = {'name' :name,'email':email,'mobile':mobile,'password' :password}

	saveData = CRUDModel().insertData(data)
	flash("Successfully Saved !")
	return redirect(url_for('crud.InsertUser'))

