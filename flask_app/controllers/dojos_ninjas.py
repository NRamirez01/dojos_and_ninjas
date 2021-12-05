from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/dojos')
def home_page():
    dojos = Dojo.all_dojos()
    return render_template("dojo.html", dojos_list = dojos)

@app.route('/addDojo', methods= ['POST'])
def add_dojo():
    data = {
        "name":request.form['dojo_name']
    }
    Dojo.add_dojo(data)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def one_dojo(id):
    data = {
        "id": id
    }
    return render_template("dojo_page.html", dojos_list = Dojo.dojo_and_ninja(data))

@app.route('/addNinja')
def ninja_form():
    dojos = Dojo.all_dojos()
    return render_template("new_ninja.html", dojos_list = dojos)

@app.route('/addNinja/submit', methods= ['POST'])
def add_ninja():
    data = {
        "dojo_id":request.form["dojo_id"],
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "age":request.form['age']
    }
    Ninja.add_ninja(data)
    dojo_id = request.form["dojo_id"]
    return redirect(f"/dojo/{dojo_id}")