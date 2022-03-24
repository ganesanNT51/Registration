from flask import Flask, request, Blueprint, jsonify, redirect, url_for,flash, render_template,session
from core.model.UserModel import UserModel
from random import randint
import datetime

from datetime import timedelta,date,datetime
from .. import Cryptography
from flask import session, app

import ast



app = Blueprint('user', __name__)

	

@app.before_request
def make_session_permanent():
	session.permanent = True
	app.permanent_session_lifetime = timedelta(minutes=1)
	session.modified = True

#home page or main page based on session..
@app.route('/', methods = ["GET", "POST"])
def Home():
	# s = Sessions()
	if request.method == "GET":
	  
		status = 1
		if session.get('user'):
			user = session.get('user')
			user_id = user['user_id']
			# the below line comment by ganesan
			# user_id = request.args.get('user_id')
			encrypted_user_id= Cryptography.encrypt(user_id)
			return redirect (url_for('user.User_index')) 
		else:
			print('in main page')
			return render_template('users/login_screen.html')

@app.route('/user_index' , methods = ["GET"])
def User_index():
	status = 1
	if session.get('user'):
		user = session.get('user')
		# user_id = request.args.get('user_id')
		user_id = user['user_id']
		encrypted_user_id= Cryptography.encrypt(user_id)
		user_output = UserModel().get_username(user_id)
		name = user_output['name']
		print("<<Welcome loggedin user >>" + name)
		name = user_output['name']  
		user_data = UserModel().get_users()
		return render_template('users/user_index.html' ,user_data= user_data,name=name)
	else :
		return redirect (url_for('user.Login'))            

@app.route('/login')
def Login():
	print('ín form')
	return render_template('users/login_screen.html')


@app.route('/register' , methods = ["GET"])
def Register():
	print('ín form')
	data =request.args.get('user_data')
	print("Data from url :")
	print (data)
	if data  is None:
		 states = UserModel().get_states()
		 return render_template('users/registration.html',states = states ,data = data)
	else :
		my_dict = ast.literal_eval(data)
		print (type(my_dict))
		states = UserModel().get_states()
		return render_template('users/registration.html',states = states ,data = my_dict)

@app.route('/register', methods = ["POST"])
def Post_register():
	if request.method == "POST":
		print('in post')
		now = datetime.now()
		# dd/mm/YY H:M:S
		dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
		name      = request.form['name']
		email     = request.form['email']
		mobile    = request.form['mobile']
		password  = request.form['password']
		confirm_password = request.form['confirm_password']
		
		gender      = request.form['gender']
		state       = request.form['state']
		

		# fetching data from form..
		data = {
			
			'name' : name,
			'email' : email,
			'mobile' : mobile,
			'state' :state,
			'gender'  : gender,
			'password' : password,
			'confirm_password' : confirm_password,
			'created_at' :[dt_string]
		}
		
		
		us = UserModel()
		#calling insert method using that object..
		if(password  == confirm_password):
			check_email = us.get_users_email(email)
			# che_email_user_id = check_email.user_id
			print(check_email)
			check_mobile = us.get_users_mobile(mobile)
			# che_mobi_user_id = check_mobile.user_id
			print(check_mobile)

			if (check_email == "success"):
				flash('Email Already Exists.')
				rem_list = ['password', 'confirm_password', 'created_at']
				[data.pop(key) for key in rem_list]
				return redirect (url_for ('user.Register' , user_data=data))

			if (check_mobile == "success"):
				flash('Mobile Number Already Exists.')
				rem_list = ['password', 'confirm_password', 'created_at']
				[data.pop(key) for key in rem_list]
				return redirect (url_for ('user.Register' , user_data=data))
			else:
				insert_users = us.insert_users(data)
				if insert_users:
					
					flash('Registration Successfully .')
					return redirect (url_for('user.Login'))
		else:
			flash('Password and confirm password mismatch ')
			return redirect (url_for('user.Register' ,  user_data=data))  

# Post_login1 
@app.route('/post_login', methods = ["GET","POST"])
def Post_login():
	print('ín form')
	if request.method == "POST":
		email     = request.form['email']
		password  = request.form['password']
		if  not email  or not password:
			flash('Please enter email and password')
			return redirect (url_for('user.Login'))
		else :
			us = UserModel()
			user_output = us.get_users_email_data(email)
			name = user_output['name']
			print("<< Loggedin user name >>" + name)
			if user_output : 
				print("form input password " + password)
				db_pass =  user_output['password']
				print(" db password " + db_pass )
				if password == db_pass:
					print(user_output['password'] + "and given password is " + password )
					user_id = user_output['user_id']
					print(  user_id )

					us.update_last_login(user_id,datetime.now());
					
					session['user'] =  user_output
					encrypted_user_id= Cryptography.encrypt(user_id)
					print(encrypted_user_id)
					# flash('Regsitration Successfully Saved ! ' )
					return redirect (url_for('user.Home',user_id= encrypted_user_id)) 

				else : 
					status = 0
					# msg = "Passsword invalid. Please check the password."
					flash('Passsword invalid. Please check the password.  ' )
					return redirect (url_for('user.Login'))

			else:
				status = 0
				msg = "Email id is not registered."

			flash("Email id is not registered." )
			return redirect (url_for('user.Login'))   
			# return jsonify({'status':status, 'message':msg})


	return render_template('users/login_screen.html')


@app.route('/adduser')
def Adduser():
	states = UserModel().get_states()
	return render_template('users/add_user.html' ,states= states)    

# logout 
@app.route('logout', methods = ["GET", "POST"])
def Logout():
	session.pop('user')
	session.pop('_flashes', None)
	return redirect(url_for('user.Login'))


@app.route('/delete_user/<int:id>' ,methods = ["GET","POST"])
def Delete_user(id):
	print("Inside in contoller delete")
	print(id)
	id = int(id)
	username = UserModel().get_username(id)
	name = username['name']
	output = UserModel().delete_user(id) 
	print(output)

	flash('User name '+ ' '+name  +' ' +' Deleted ! ' )
	return redirect (url_for('user.User_index'))

@app.route('/edit_user/<int:id>',methods = ["GET","POST"])
def Edit_user(id):
	id = int(id)
	output = UserModel().edit_user(id) 
	states = UserModel().get_states()
	return render_template('users/edit_user.html',data = output, states=states, str=str,type=type,id = id)

# Post_edituser
@app.route('/post_edituser/<int:id>',methods = ["GET","POST"])
def Post_edituser(id):
	id = int(id)
	if request.method == "POST":
		now = datetime.now()
		dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
		name      = request.form['name']
		email     = request.form['email']
		mobile    = request.form['mobile']
		password  = request.form['password']
		confirm_password = request.form['confirm_password']
		
		gender      = request.form['gender']
		state       = request.form['state']
		

		# fetching data from form..
		data = {
			
			'name' : name,
			'email' : email,
			'mobile' : mobile,
			'state' :state,
			'gender'  : gender,
			'password' : password,
			'confirm_password' : confirm_password,
			'updated_at' :[dt_string]
		}
		if(password  == confirm_password):
			
			check_email  = UserModel().check_users_email_for_update(email,id)
			check_mobile = UserModel().check_users_mobile_for_update(mobile,id)
			print("<<Email count  >>")
			# part = check_email.replace(')', '')
			print((check_email['email_count']))
			if (check_email['email_count'] == 1):
				flash('This email already exist ')
				return redirect (url_for('user.Edit_user' ,  id=id))
			if (check_mobile['mobile_count'] ==1):
				flash('This mobile already exist ')
				return redirect (url_for('user.Edit_user' ,  id=id))
			output = UserModel().update_user(id,data)
			if output == "success":
				flash("Updated !")
				return redirect( url_for('user.User_index'))
		else:
			flash('Password and confirm password mismatch ')
			return redirect (url_for('user.Edit_user' ,  id=id))
				 
		

				



