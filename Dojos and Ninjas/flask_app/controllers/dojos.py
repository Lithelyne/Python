from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja



@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template("dojos.html",dojos=Dojo.get_all())

@app.route('/dojos/show/<int:id>')
def show_dojo(id):
    data = {"id": id}
    dojo = Dojo.get_by_id(id)
    ninjas = Dojo.get_ninjas_by_dojo_id(data)
    print(dojo)  # Add this line to check the value of dojo
    return render_template('show_dojos.html', dojo=dojo, ninjas=ninjas)

@app.route('/dojos/create', methods=['POST'])
def create():
    
    # Get the value of the "dojo_name" input field from the form
    dojo_name = request.form.get("dojo_name")

    # Create a dictionary with the correct key name
    data = {"name": dojo_name}

    # Call the Dojo.save() method with the formatted data dictionary
    Dojo.save(data)

    return redirect('/dojos')

