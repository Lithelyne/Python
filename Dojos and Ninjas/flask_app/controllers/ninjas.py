from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo




@app.route('/ninja/new')
def users():
    return render_template("ninjas.html",dojos=Dojo.get_all(), ninjas=Ninja.get_all())

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    # data = {
    #     "first_name":request.form['first_name'],
    #     "last_name":request.form['last_name'],
    #     "age":request.form['age'],
    #     # "dojo_id":request.form['dojo_id']
    # }
    # print(request.form['dojo_id'])
    Ninja.save(request.form)
    return redirect('/dojos')