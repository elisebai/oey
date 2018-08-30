from myapp import app
from models import db, Post, Info
from forms import LoginForm, PostForm, InfoForm
from flask import render_template, send_file, url_for, request, redirect, Flask
from sqlalchemy import func, extract, and_
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy


@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/listing',methods=['GET', 'POST'])
def listing():
    return render_template('listing.html')

@app.route('/boat',methods=['GET', 'POST'])
def boat():
    return render_template('boat.html')

@app.route('/booking1',methods=['GET', 'POST'])
def booking1():
    return render_template('booking1.html')

@app.route('/booking2',methods=['GET', 'POST'])
def booking2():
    return render_template('booking2.html')

@app.route('/booking3',methods=['GET', 'POST'])
def booking3():
    return render_template('booking3.html')

# @app.route('/listing',methods=['GET', 'POST'])
# def listing():
#     return render_template('listing.html')

# @app.route('/listing35',methods=['GET', 'POST'])
# def listing35():
#     return render_template('listing35.html')

# @app.route('/listing45',methods=['GET', 'POST'])
# def listing45():
#     return render_template('listing45.html')

# @app.route('/listing60',methods=['GET', 'POST'])
# def listing60():
#     return render_template('listing60.html')

# @app.route('/listing80',methods=['GET', 'POST'])
# def listing80():
#     return render_template('listing80.html')

# @app.route('/listing120',methods=['GET', 'POST'])
# def listing120():
#     return render_template('listing120.html')

# @app.route('/boat',methods=['GET', 'POST'])
# def boat():
#     return render_template('boat.html')


# @app.route('/boat/sz/2',methods=['GET', 'POST'])
# def boat1():

# 	post = Post.query.filter_by(boatname='DD号').first()

# 	return render_template('boat2.html', post=post)

# @app.route('/boattest',methods=['GET', 'POST'])
# def boattest():

# 	post = Post.query.filter_by(boatname='DD号').first()

# 	return render_template('boattest.html', post=post)

# @app.route('/boat/sz/3',methods=['GET', 'POST'])
# def boat2():

# 	post = Post.query.filter_by(boatname='EE号').first()

# 	return render_template('boat3.html', post=post)

# @app.route('/boat/sz/4',methods=['GET', 'POST'])
# def boat3():

# 	post = Post.query.filter_by(boatname='EE号').first()

# 	return render_template('boat4.html', post=post)

# @app.route('/boat/sz/5',methods=['GET', 'POST'])
# def boat4():

# 	post = Post.query.filter_by(boatname='EE号').first()

# 	return render_template('boat5.html', post=post)

# @app.route('/boat/sz/6',methods=['GET', 'POST'])
# def boat5():

# 	post = Post.query.filter_by(boatname='EE号').first()

# 	return render_template('boat6.html', post=post)



# @app.route('/inquiry',methods=['GET', 'POST'])
# def inquiry():

# 	# post = Post.query.filter_by(boatname='EE号').first()

#     form = InfoForm()

#     if request.method == 'POST':
#         info = Info(interestedboat=form.interestedboat.data,destination=form.destination.data,sex=form.sex.data,name=form.name.data, email=form.email.data, phone=form.phone.data, availabletime=form.availabletime.data, notes=form.notes.data)
#         db.session.add(info)
#         db.session.commit()
#         return redirect(url_for('finish'))
#     return render_template('inquiry.html', form=form)

# @app.route('/finish',methods=['GET', 'POST'])
# def finish():


#     return render_template('finish.html')

# @app.route('/testcalender',methods=['GET', 'POST'])
# def testcalender():


#     return render_template('testcalender.html')

# @app.route("/post/new", methods=['GET', 'POST'])
# def new_post():

#     form = PostForm()

#     if request.method == 'POST':
#         post = Post(boatname=form.boatname.data,price=form.price.data,
# 		length=form.length.data,numberofguests=form.numberofguests.data, numberofcabins=form.numberofcabins.data, bodylength=form.bodylength.data, 
# 		beamlength=form.beamlength.data, draft=form.draft.data,
# 		crewnumber=form.crewnumber.data,builtyear=form.builtyear.data, producer=form.producer.data, engine=form.engine.data,  cruisespeed=form.cruisespeed.data
# 		)
#         db.session.add(post)
#         db.session.commit()
#         return redirect(url_for('finish'))


#     return render_template('create_post.html', form=form)

# @app.route('/test',methods=['GET', 'POST'])
# def test():

# 	# post = Post.query.filter_by(boatname='EE号').first()

#     form = InfoForm()

#     if request.method == 'POST':
#         info = Info(interestedboat=form.interestedboat.data,destination=form.destination.data,sex=form.sex.data,name=form.name.data, email=form.email.data, phone=form.phone.data, availabletime=form.availabletime.data, notes=form.notes.data)
#         db.session.add(info)
#         db.session.commit()
#         return redirect(url_for('finish'))
#     return render_template('test.html', form=form)


# @app.route('/test2',methods=['GET', 'POST'])
# def test2():

# 	# post = Post.query.filter_by(boatname='EE号').first()

#     form = InfoForm()

#     if request.method == 'POST':
#         info = Info(interestedboat=form.interestedboat.data,destination=form.destination.data,sex=form.sex.data,name=form.name.data, email=form.email.data, phone=form.phone.data, availabletime=form.availabletime.data, notes=form.notes.data)
#         db.session.add(info)
#         db.session.commit()
#         return redirect(url_for('finish'))
#     return render_template('test2.html', form=form)

# @app.route("/orders", methods=['GET', 'POST'])
# def orders():

#     # posts = Post.query.filter_by(if_agree=False).order_by('date_created desc').filter().all() + Post.query.filter_by(if_agree=None).order_by('date_created desc').all()
#     # posts = Post.query.filter_by(if_agree=None).order_by('date_created desc').filter().all()

#     infos = Info.query.all()



#     return render_template('orders.html', infos=infos)





# @app.route('/login')
# def login():
#     form = LoginForm()
#     return render_template('index.html', form=form)

# @app.route('/login/business', methods=['GET', 'POST'])
# def business():
#     return render_template('business.html')

# @app.route('/file-downloads/')
# def file_downloads():
# 	try:
# 		return render_template('downloads.html')
# 	except Exception as e:
# 		return str(e)

# @app.route('/return-files/')
# def return_files_tut():
# 	try:
# 		return send_file('./files/Vision.exe', as_attachment=True, attachment_filename='Vision.exe')
# 	except Exception as e:
# 		return str(e)
